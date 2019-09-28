# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: unittest\main.py
"""Unittest main program"""
import sys, argparse, os
from . import loader, runner
from .signals import installHandler
__unittest = True
MAIN_EXAMPLES = 'Examples:\n  %(prog)s test_module               - run tests from test_module\n  %(prog)s module.TestClass          - run tests from module.TestClass\n  %(prog)s module.Class.test_method  - run specified test method\n  %(prog)s path/to/test_file.py      - run tests from test_file.py\n'
MODULE_EXAMPLES = "Examples:\n  %(prog)s                           - run default set of tests\n  %(prog)s MyTestSuite               - run suite 'MyTestSuite'\n  %(prog)s MyTestCase.testSomething  - run MyTestCase.testSomething\n  %(prog)s MyTestCase                - run all 'test*' test methods\n                                       in MyTestCase\n"

def _convert_name(name):
    if os.path.isfile(name):
        if name.lower().endswith('.py'):
            if os.path.isabs(name):
                rel_path = os.path.relpath(name, os.getcwd())
                if os.path.isabs(rel_path) or rel_path.startswith(os.pardir):
                    return name
                name = rel_path
        return name[:-3].replace('\\', '.').replace('/', '.')
    else:
        return name


def _convert_names(names):
    return [_convert_name(name) for name in names]


def _convert_select_pattern(pattern):
    if '*' not in pattern:
        pattern = '*%s*' % pattern
    return pattern


class TestProgram(object):
    r"""'A command-line program that runs a set of tests; this is primarily\n       for making test modules conveniently executable.\n    '"""
    module = None
    verbosity = 1
    failfast = catchbreak = buffer = progName = warnings = testNamePatterns = None
    _discovery_parser = None

    def __init__(self, module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=loader.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None, warnings=None, *, tb_locals=False):
        if isinstance(module, str):
            self.module = __import__(module)
            for part in module.split('.')[1:]:
                self.module = getattr(self.module, part)

        else:
            self.module = module
        if argv is None:
            argv = sys.argv
        self.exit = exit
        self.failfast = failfast
        self.catchbreak = catchbreak
        self.verbosity = verbosity
        self.buffer = buffer
        self.tb_locals = tb_locals
        if warnings is None:
            if not sys.warnoptions:
                self.warnings = 'default'
            else:
                self.warnings = warnings
            self.defaultTest = defaultTest
            self.testRunner = testRunner
            self.testLoader = testLoader
            self.progName = os.path.basename(argv[0])
            self.parseArgs(argv)
            self.runTests()

    def usageExit(self, msg=None):
        if msg:
            print(msg)
        if self._discovery_parser is None:
            self._initArgParsers()
        self._print_help()
        sys.exit(2)

    def _print_help(self, *args, **kwargs):
        if self.module is None:
            print(self._main_parser.format_help())
            print(MAIN_EXAMPLES % {'prog': self.progName})
            self._discovery_parser.print_help()
        else:
            print(self._main_parser.format_help())
            print(MODULE_EXAMPLES % {'prog': self.progName})

    def parseArgs(self, argv):
        self._initArgParsers()
        if self.module is None:
            pass
        if len(argv) > 1:
            if argv[1].lower() == 'discover':
                self._do_discovery(argv[2:])
                return
            self._main_parser.parse_args(argv[1:], self)
            if not self.tests:
                self._do_discovery([])
                return
        else:
            self._main_parser.parse_args(argv[1:], self)
        if self.tests:
            self.testNames = _convert_names(self.tests)
            if __name__ == '__main__':
                self.module = None
            elif self.defaultTest is None:
                self.testNames = None
            elif isinstance(self.defaultTest, str):
                self.testNames = (
                 self.defaultTest,)
            else:
                self.testNames = list(self.defaultTest)
            self.createTests()

    def createTests(self, from_discovery=False, Loader=None):
        if self.testNamePatterns:
            self.testLoader.testNamePatterns = self.testNamePatterns
        if from_discovery:
            loader = self.testLoader if Loader is None else Loader()
            self.test = loader.discover(self.start, self.pattern, self.top)
        elif self.testNames is None:
            self.test = self.testLoader.loadTestsFromModule(self.module)
        else:
            self.test = self.testLoader.loadTestsFromNames(self.testNames, self.module)

    def _initArgParsers(self):
        parent_parser = self._getParentArgParser()
        self._main_parser = self._getMainArgParser(parent_parser)
        self._discovery_parser = self._getDiscoveryArgParser(parent_parser)

    def _getParentArgParser(self):
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('-v', '--verbose', dest='verbosity', action='store_const',
          const=2,
          help='Verbose output')
        parser.add_argument('-q', '--quiet', dest='verbosity', action='store_const',
          const=0,
          help='Quiet output')
        parser.add_argument('--locals', dest='tb_locals', action='store_true',
          help='Show local variables in tracebacks')
        if self.failfast is None:
            parser.add_argument('-f', '--failfast', dest='failfast', action='store_true',
              help='Stop on first fail or error')
            self.failfast = False
        if self.catchbreak is None:
            parser.add_argument('-c', '--catch', dest='catchbreak', action='store_true',
              help='Catch Ctrl-C and display results so far')
            self.catchbreak = False
        if self.buffer is None:
            parser.add_argument('-b', '--buffer', dest='buffer', action='store_true',
              help='Buffer stdout and stderr during tests')
            self.buffer = False
        if self.testNamePatterns is None:
            parser.add_argument('-k', dest='testNamePatterns', action='append',
              type=_convert_select_pattern,
              help='Only run tests which match the given substring')
            self.testNamePatterns = []
        return parser

    def _getMainArgParser(self, parent):
        parser = argparse.ArgumentParser(parents=[parent])
        parser.prog = self.progName
        parser.print_help = self._print_help
        parser.add_argument('tests', nargs='*', help='a list of any number of test modules, classes and test methods.')
        return parser

    def _getDiscoveryArgParser(self, parent):
        parser = argparse.ArgumentParser(parents=[parent])
        parser.prog = '%s discover' % self.progName
        parser.epilog = 'For test discovery all test modules must be importable from the top level directory of the project.'
        parser.add_argument('-s', '--start-directory', dest='start', help="Directory to start discovery ('.' default)")
        parser.add_argument('-p', '--pattern', dest='pattern', help="Pattern to match tests ('test*.py' default)")
        parser.add_argument('-t', '--top-level-directory', dest='top', help='Top level directory of project (defaults to start directory)')
        for arg in ('start', 'pattern', 'top'):
            parser.add_argument(arg, nargs='?', default=(argparse.SUPPRESS),
              help=(argparse.SUPPRESS))

        return parser

    def _do_discovery(self, argv, Loader=None):
        self.start = '.'
        self.pattern = 'test*.py'
        self.top = None
        if argv is not None:
            if self._discovery_parser is None:
                self._initArgParsers()
            self._discovery_parser.parse_args(argv, self)
        self.createTests(from_discovery=True, Loader=Loader)

    def runTests(self):
        if self.catchbreak:
            installHandler()
        if self.testRunner is None:
            self.testRunner = runner.TextTestRunner
        if isinstance(self.testRunner, type):
            try:
                try:
                    testRunner = self.testRunner(verbosity=(self.verbosity), failfast=(self.failfast),
                      buffer=(self.buffer),
                      warnings=(self.warnings),
                      tb_locals=(self.tb_locals))
                except TypeError:
                    testRunner = self.testRunner(verbosity=(self.verbosity), failfast=(self.failfast),
                      buffer=(self.buffer),
                      warnings=(self.warnings))

            except TypeError:
                testRunner = self.testRunner()

        else:
            testRunner = self.testRunner
        self.result = testRunner.run(self.test)
        if self.exit:
            sys.exit(not self.result.wasSuccessful())


main = TestProgram
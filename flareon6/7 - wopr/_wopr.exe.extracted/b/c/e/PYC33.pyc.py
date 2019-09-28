# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: importlib\machinery.py
"""The machinery of importlib: finders, loaders, hooks, etc."""
import _imp
from ._bootstrap import ModuleSpec
from ._bootstrap import BuiltinImporter
from ._bootstrap import FrozenImporter
from ._bootstrap_external import SOURCE_SUFFIXES, DEBUG_BYTECODE_SUFFIXES, OPTIMIZED_BYTECODE_SUFFIXES, BYTECODE_SUFFIXES, EXTENSION_SUFFIXES
from ._bootstrap_external import WindowsRegistryFinder
from ._bootstrap_external import PathFinder
from ._bootstrap_external import FileFinder
from ._bootstrap_external import SourceFileLoader
from ._bootstrap_external import SourcelessFileLoader
from ._bootstrap_external import ExtensionFileLoader

def all_suffixes():
    """Returns a list of all recognized module suffixes for this process"""
    return SOURCE_SUFFIXES + BYTECODE_SUFFIXES + EXTENSION_SUFFIXES
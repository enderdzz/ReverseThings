# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: difflib.py
"""
Module difflib -- helpers for computing deltas between objects.

Function get_close_matches(word, possibilities, n=3, cutoff=0.6):
    Use SequenceMatcher to return list of the best "good enough" matches.

Function context_diff(a, b):
    For two lists of strings, return a delta in context diff format.

Function ndiff(a, b):
    Return a delta: the difference between `a` and `b` (lists of strings).

Function restore(delta, which):
    Return one of the two sequences that generated an ndiff delta.

Function unified_diff(a, b):
    For two lists of strings, return a delta in unified diff format.

Class SequenceMatcher:
    A flexible class for comparing pairs of sequences of any type.

Class Differ:
    For producing human-readable deltas from sequences of lines of text.

Class HtmlDiff:
    For producing HTML side by side comparison with change highlights.
"""
__all__ = [
 'get_close_matches', 'ndiff', 'restore', 'SequenceMatcher',
 'Differ', 'IS_CHARACTER_JUNK', 'IS_LINE_JUNK', 'context_diff',
 'unified_diff', 'diff_bytes', 'HtmlDiff', 'Match']
from heapq import nlargest as _nlargest
from collections import namedtuple as _namedtuple
Match = _namedtuple('Match', 'a b size')

def _calculate_ratio(matches, length):
    if length:
        return 2.0 * matches / length
    else:
        return 1.0


class SequenceMatcher:
    r"""'\n    SequenceMatcher is a flexible class for comparing pairs of sequences of\n    any type, so long as the sequence elements are hashable.  The basic\n    algorithm predates, and is a little fancier than, an algorithm\n    published in the late 1980\'s by Ratcliff and Obershelp under the\n    hyperbolic name "gestalt pattern matching".  The basic idea is to find\n    the longest contiguous matching subsequence that contains no "junk"\n    elements (R-O doesn\'t address junk).  The same idea is then applied\n    recursively to the pieces of the sequences to the left and to the right\n    of the matching subsequence.  This does not yield minimal edit\n    sequences, but does tend to yield matches that "look right" to people.\n\n    SequenceMatcher tries to compute a "human-friendly diff" between two\n    sequences.  Unlike e.g. UNIX(tm) diff, the fundamental notion is the\n    longest *contiguous* & junk-free matching subsequence.  That\'s what\n    catches peoples\' eyes.  The Windows(tm) windiff has another interesting\n    notion, pairing up elements that appear uniquely in each sequence.\n    That, and the method here, appear to yield more intuitive difference\n    reports than does diff.  This method appears to be the least vulnerable\n    to synching up on blocks of "junk lines", though (like blank lines in\n    ordinary text files, or maybe "<P>" lines in HTML files).  That may be\n    because this is the only method of the 3 that has a *concept* of\n    "junk" <wink>.\n\n    Example, comparing two strings, and considering blanks to be "junk":\n\n    >>> s = SequenceMatcher(lambda x: x == " ",\n    ...                     "private Thread currentThread;",\n    ...                     "private volatile Thread currentThread;")\n    >>>\n\n    .ratio() returns a float in [0, 1], measuring the "similarity" of the\n    sequences.  As a rule of thumb, a .ratio() value over 0.6 means the\n    sequences are close matches:\n\n    >>> print(round(s.ratio(), 3))\n    0.866\n    >>>\n\n    If you\'re only interested in where the sequences match,\n    .get_matching_blocks() is handy:\n\n    >>> for block in s.get_matching_blocks():\n    ...     print("a[%d] and b[%d] match for %d elements" % block)\n    a[0] and b[0] match for 8 elements\n    a[8] and b[17] match for 21 elements\n    a[29] and b[38] match for 0 elements\n\n    Note that the last tuple returned by .get_matching_blocks() is always a\n    dummy, (len(a), len(b), 0), and this is the only case in which the last\n    tuple element (number of elements matched) is 0.\n\n    If you want to know how to change the first sequence into the second,\n    use .get_opcodes():\n\n    >>> for opcode in s.get_opcodes():\n    ...     print("%6s a[%d:%d] b[%d:%d]" % opcode)\n     equal a[0:8] b[0:8]\n    insert a[8:8] b[8:17]\n     equal a[8:29] b[17:38]\n\n    See the Differ class for a fancy human-friendly file differencer, which\n    uses SequenceMatcher both to compare sequences of lines, and to compare\n    sequences of characters within similar (near-matching) lines.\n\n    See also function get_close_matches() in this module, which shows how\n    simple code building on SequenceMatcher can be used to do useful work.\n\n    Timing:  Basic R-O is cubic time worst case and quadratic time expected\n    case.  SequenceMatcher is quadratic time for the worst case and has\n    expected-case behavior dependent in a complicated way on how many\n    elements the sequences have in common; best case time is linear.\n\n    Methods:\n\n    __init__(isjunk=None, a=\'\', b=\'\')\n        Construct a SequenceMatcher.\n\n    set_seqs(a, b)\n        Set the two sequences to be compared.\n\n    set_seq1(a)\n        Set the first sequence to be compared.\n\n    set_seq2(b)\n        Set the second sequence to be compared.\n\n    find_longest_match(alo, ahi, blo, bhi)\n        Find longest matching block in a[alo:ahi] and b[blo:bhi].\n\n    get_matching_blocks()\n        Return list of triples describing matching subsequences.\n\n    get_opcodes()\n        Return list of 5-tuples describing how to turn a into b.\n\n    ratio()\n        Return a measure of the sequences\' similarity (float in [0,1]).\n\n    quick_ratio()\n        Return an upper bound on .ratio() relatively quickly.\n\n    real_quick_ratio()\n        Return an upper bound on ratio() very quickly.\n    '"""

    def __init__(self, isjunk=None, a='', b='', autojunk=True):
        r"""Construct a SequenceMatcher.

        Optional arg isjunk is None (the default), or a one-argument
        function that takes a sequence element and returns true iff the
        element is junk.  None is equivalent to passing "lambda x: 0", i.e.
        no elements are considered to be junk.  For example, pass
            lambda x: x in " \t"
        if you're comparing lines as sequences of characters, and don't
        want to synch up on blanks or hard tabs.

        Optional arg a is the first of two sequences to be compared.  By
        default, an empty string.  The elements of a must be hashable.  See
        also .set_seqs() and .set_seq1().

        Optional arg b is the second of two sequences to be compared.  By
        default, an empty string.  The elements of b must be hashable. See
        also .set_seqs() and .set_seq2().

        Optional arg autojunk should be set to False to disable the
        "automatic junk heuristic" that treats popular elements as junk
        (see module documentation for more information).
        """
        self.isjunk = isjunk
        self.a = self.b = None
        self.autojunk = autojunk
        self.set_seqs(a, b)

    def set_seqs(self, a, b):
        """Set the two sequences to be compared.

        >>> s = SequenceMatcher()
        >>> s.set_seqs("abcd", "bcde")
        >>> s.ratio()
        0.75
        """
        self.set_seq1(a)
        self.set_seq2(b)

    def set_seq1(self, a):
        """Set the first sequence to be compared.

        The second sequence to be compared is not changed.

        >>> s = SequenceMatcher(None, "abcd", "bcde")
        >>> s.ratio()
        0.75
        >>> s.set_seq1("bcde")
        >>> s.ratio()
        1.0
        >>>

        SequenceMatcher computes and caches detailed information about the
        second sequence, so if you want to compare one sequence S against
        many sequences, use .set_seq2(S) once and call .set_seq1(x)
        repeatedly for each of the other sequences.

        See also set_seqs() and set_seq2().
        """
        if a is self.a:
            return
        self.a = a
        self.matching_blocks = self.opcodes = None

    def set_seq2(self, b):
        """Set the second sequence to be compared.

        The first sequence to be compared is not changed.

        >>> s = SequenceMatcher(None, "abcd", "bcde")
        >>> s.ratio()
        0.75
        >>> s.set_seq2("abcd")
        >>> s.ratio()
        1.0
        >>>

        SequenceMatcher computes and caches detailed information about the
        second sequence, so if you want to compare one sequence S against
        many sequences, use .set_seq2(S) once and call .set_seq1(x)
        repeatedly for each of the other sequences.

        See also set_seqs() and set_seq1().
        """
        if b is self.b:
            return
        self.b = b
        self.matching_blocks = self.opcodes = None
        self.fullbcount = None
        self._SequenceMatcher__chain_b()

    def __chain_b(self):
        b = self.b
        self.b2j = b2j = {}
        for i, elt in enumerate(b):
            indices = b2j.setdefault(elt, [])
            indices.append(i)

        self.bjunk = junk = set()
        isjunk = self.isjunk
        if isjunk:
            for elt in b2j.keys():
                if isjunk(elt):
                    junk.add(elt)

            for elt in junk:
                del b2j[elt]

        self.bpopular = popular = set()
        n = len(b)
        if self.autojunk:
            pass
        if n >= 200:
            ntest = n // 100 + 1
            for elt, idxs in b2j.items():
                if len(idxs) > ntest:
                    popular.add(elt)

            for elt in popular:
                del b2j[elt]

    def find_longest_match(self, alo, ahi, blo, bhi):
        """Find longest matching block in a[alo:ahi] and b[blo:bhi].

        If isjunk is not defined:

        Return (i,j,k) such that a[i:i+k] is equal to b[j:j+k], where
            alo <= i <= i+k <= ahi
            blo <= j <= j+k <= bhi
        and for all (i',j',k') meeting those conditions,
            k >= k'
            i <= i'
            and if i == i', j <= j'

        In other words, of all maximal matching blocks, return one that
        starts earliest in a, and of all those maximal matching blocks that
        start earliest in a, return the one that starts earliest in b.

        >>> s = SequenceMatcher(None, " abcd", "abcd abcd")
        >>> s.find_longest_match(0, 5, 0, 9)
        Match(a=0, b=4, size=5)

        If isjunk is defined, first the longest matching block is
        determined as above, but with the additional restriction that no
        junk element appears in the block.  Then that block is extended as
        far as possible by matching (only) junk elements on both sides.  So
        the resulting block never matches on junk except as identical junk
        happens to be adjacent to an "interesting" match.

        Here's the same example as before, but considering blanks to be
        junk.  That prevents " abcd" from matching the " abcd" at the tail
        end of the second sequence directly.  Instead only the "abcd" can
        match, and matches the leftmost "abcd" in the second sequence:

        >>> s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
        >>> s.find_longest_match(0, 5, 0, 9)
        Match(a=1, b=0, size=4)

        If no blocks match, return (alo, blo, 0).

        >>> s = SequenceMatcher(None, "ab", "c")
        >>> s.find_longest_match(0, 2, 0, 1)
        Match(a=0, b=0, size=0)
        """
        a, b, b2j, isbjunk = (
         self.a, self.b, self.b2j, self.bjunk.__contains__)
        besti, bestj, bestsize = alo, blo, 0
        j2len = {}
        nothing = []
        for i in range(alo, ahi):
            j2lenget = j2len.get
            newj2len = {}
            for j in b2j.get(a[i], nothing):
                if j < blo:
                    continue
                if j >= bhi:
                    break
                k = newj2len[j] = j2lenget(j - 1, 0) + 1
                if k > bestsize:
                    besti, bestj, bestsize = i - k + 1, j - k + 1, k

            j2len = newj2len

        while besti > alo:
            if bestj > blo:
                if not isbjunk(b[(bestj - 1)]):
                    besti, bestj, bestsize = a[(besti - 1)] == b[(bestj - 1)] and besti - 1, bestj - 1, bestsize + 1

        while besti + bestsize < ahi:
            if bestj + bestsize < bhi:
                if not isbjunk(b[(bestj + bestsize)]):
                    if a[(besti + bestsize)] == b[(bestj + bestsize)]:
                        bestsize += 1

        while besti > alo:
            if bestj > blo:
                besti, bestj, bestsize = isbjunk(b[(bestj - 1)]) and a[(besti - 1)] == b[(bestj - 1)] and besti - 1, bestj - 1, bestsize + 1

        while besti + bestsize < ahi:
            if bestj + bestsize < bhi:
                bestsize = isbjunk(b[(bestj + bestsize)]) and a[(besti + bestsize)] == b[(bestj + bestsize)] and bestsize + 1

        return Match(besti, bestj, bestsize)

    def get_matching_blocks(self):
        """Return list of triples describing matching subsequences.

        Each triple is of the form (i, j, n), and means that
        a[i:i+n] == b[j:j+n].  The triples are monotonically increasing in
        i and in j.  New in Python 2.5, it's also guaranteed that if
        (i, j, n) and (i', j', n') are adjacent triples in the list, and
        the second is not the last triple in the list, then i+n != i' or
        j+n != j'.  IOW, adjacent triples never describe adjacent equal
        blocks.

        The last triple is a dummy, (len(a), len(b), 0), and is the only
        triple with n==0.

        >>> s = SequenceMatcher(None, "abxcd", "abcd")
        >>> list(s.get_matching_blocks())
        [Match(a=0, b=0, size=2), Match(a=3, b=2, size=2), Match(a=5, b=4, size=0)]
        """
        if self.matching_blocks is not None:
            return self.matching_blocks
        else:
            la, lb = len(self.a), len(self.b)
            queue = [
             (
              0, la, 0, lb)]
            matching_blocks = []
            while 1:
                if queue:
                    alo, ahi, blo, bhi = queue.pop()
                    i, j, k = x = self.find_longest_match(alo, ahi, blo, bhi)
                    if k:
                        matching_blocks.append(x)
                    if alo < i:
                        if blo < j:
                            queue.append((alo, i, blo, j))
                        if i + k < ahi:
                            if j + k < bhi:
                                queue.append((i + k, ahi, j + k, bhi))

            matching_blocks.sort()
            i1 = j1 = k1 = 0
            non_adjacent = []
            for i2, j2, k2 in matching_blocks:
                if i1 + k1 == i2:
                    if j1 + k1 == j2:
                        k1 += k2
                elif k1:
                    non_adjacent.append((i1, j1, k1))
                else:
                    i1, j1, k1 = i2, j2, k2

            if k1:
                non_adjacent.append((i1, j1, k1))
            non_adjacent.append((la, lb, 0))
            self.matching_blocks = list(map(Match._make, non_adjacent))
            return self.matching_blocks

    def get_opcodes(self):
        """Return list of 5-tuples describing how to turn a into b.

        Each tuple is of the form (tag, i1, i2, j1, j2).  The first tuple
        has i1 == j1 == 0, and remaining tuples have i1 == the i2 from the
        tuple preceding it, and likewise for j1 == the previous j2.

        The tags are strings, with these meanings:

        'replace':  a[i1:i2] should be replaced by b[j1:j2]
        'delete':   a[i1:i2] should be deleted.
                    Note that j1==j2 in this case.
        'insert':   b[j1:j2] should be inserted at a[i1:i1].
                    Note that i1==i2 in this case.
        'equal':    a[i1:i2] == b[j1:j2]

        >>> a = "qabxcd"
        >>> b = "abycdf"
        >>> s = SequenceMatcher(None, a, b)
        >>> for tag, i1, i2, j1, j2 in s.get_opcodes():
        ...    print(("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %
        ...           (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])))
         delete a[0:1] (q) b[0:0] ()
          equal a[1:3] (ab) b[0:2] (ab)
        replace a[3:4] (x) b[2:3] (y)
          equal a[4:6] (cd) b[3:5] (cd)
         insert a[6:6] () b[5:6] (f)
        """
        if self.opcodes is not None:
            return self.opcodes
        else:
            i = j = 0
            self.opcodes = answer = []
            for ai, bj, size in self.get_matching_blocks():
                tag = ''
                if i < ai:
                    if j < bj:
                        tag = 'replace'
                    elif i < ai:
                        tag = 'delete'
                    elif j < bj:
                        tag = 'insert'
                    if tag:
                        answer.append((tag, i, ai, j, bj))
                    i, j = ai + size, bj + size
                    if size:
                        answer.append(('equal', ai, i, bj, j))

            return answer

    def get_grouped_opcodes(self, n=3):
        """ Isolate change clusters by eliminating ranges with no changes.

        Return a generator of groups with up to n lines of context.
        Each group is in the same format as returned by get_opcodes().

        >>> from pprint import pprint
        >>> a = list(map(str, range(1,40)))
        >>> b = a[:]
        >>> b[8:8] = ['i']     # Make an insertion
        >>> b[20] += 'x'       # Make a replacement
        >>> b[23:28] = []      # Make a deletion
        >>> b[30] += 'y'       # Make another replacement
        >>> pprint(list(SequenceMatcher(None,a,b).get_grouped_opcodes()))
        [[('equal', 5, 8, 5, 8), ('insert', 8, 8, 8, 9), ('equal', 8, 11, 9, 12)],
         [('equal', 16, 19, 17, 20),
          ('replace', 19, 20, 20, 21),
          ('equal', 20, 22, 21, 23),
          ('delete', 22, 27, 23, 23),
          ('equal', 27, 30, 23, 26)],
         [('equal', 31, 34, 27, 30),
          ('replace', 34, 35, 30, 31),
          ('equal', 35, 38, 31, 34)]]
        """
        codes = self.get_opcodes()
        if not codes:
            codes = [
             ('equal', 0, 1, 0, 1)]
        if codes[0][0] == 'equal':
            tag, i1, i2, j1, j2 = codes[0]
            codes[0] = (tag, max(i1, i2 - n), i2, max(j1, j2 - n), j2)
        if codes[(-1)][0] == 'equal':
            tag, i1, i2, j1, j2 = codes[(-1)]
            codes[-1] = (tag, i1, min(i2, i1 + n), j1, min(j2, j1 + n))
        nn = n + n
        group = []
        for tag, i1, i2, j1, j2 in codes:
            if tag == 'equal':
                if i2 - i1 > nn:
                    group.append((tag, i1, min(i2, i1 + n), j1, min(j2, j1 + n)))
                    yield group
                    group = []
                    i1, j1 = max(i1, i2 - n), max(j1, j2 - n)
                group.append((tag, i1, i2, j1, j2))

        if group:
            pass
        if not (len(group) == 1 and group[0][0] == 'equal'):
            yield group

    def ratio(self):
        """Return a measure of the sequences' similarity (float in [0,1]).

        Where T is the total number of elements in both sequences, and
        M is the number of matches, this is 2.0*M / T.
        Note that this is 1 if the sequences are identical, and 0 if
        they have nothing in common.

        .ratio() is expensive to compute if you haven't already computed
        .get_matching_blocks() or .get_opcodes(), in which case you may
        want to try .quick_ratio() or .real_quick_ratio() first to get an
        upper bound.

        >>> s = SequenceMatcher(None, "abcd", "bcde")
        >>> s.ratio()
        0.75
        >>> s.quick_ratio()
        0.75
        >>> s.real_quick_ratio()
        1.0
        """
        matches = sum(triple[(-1)] for triple in self.get_matching_blocks())
        return _calculate_ratio(matches, len(self.a) + len(self.b))

    def quick_ratio(self):
        """Return an upper bound on ratio() relatively quickly.

        This isn't defined beyond that it is an upper bound on .ratio(), and
        is faster to compute.
        """
        if self.fullbcount is None:
            self.fullbcount = fullbcount = {}
            for elt in self.b:
                fullbcount[elt] = fullbcount.get(elt, 0) + 1

        fullbcount = self.fullbcount
        avail = {}
        availhas, matches = avail.__contains__, 0
        for elt in self.a:
            if availhas(elt):
                numb = avail[elt]
            else:
                numb = fullbcount.get(elt, 0)
            avail[elt] = numb - 1
            if numb > 0:
                matches = matches + 1

        return _calculate_ratio(matches, len(self.a) + len(self.b))

    def real_quick_ratio(self):
        """Return an upper bound on ratio() very quickly.

        This isn't defined beyond that it is an upper bound on .ratio(), and
        is faster to compute than either .ratio() or .quick_ratio().
        """
        la, lb = len(self.a), len(self.b)
        return _calculate_ratio(min(la, lb), la + lb)


def get_close_matches(word, possibilities, n=3, cutoff=0.6):
    """Use SequenceMatcher to return list of the best "good enough" matches.

    word is a sequence for which close matches are desired (typically a
    string).

    possibilities is a list of sequences against which to match word
    (typically a list of strings).

    Optional arg n (default 3) is the maximum number of close matches to
    return.  n must be > 0.

    Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
    that don't score at least that similar to word are ignored.

    The best (no more than n) matches among the possibilities are returned
    in a list, sorted by similarity score, most similar first.

    >>> get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
    ['apple', 'ape']
    >>> import keyword as _keyword
    >>> get_close_matches("wheel", _keyword.kwlist)
    ['while']
    >>> get_close_matches("Apple", _keyword.kwlist)
    []
    >>> get_close_matches("accept", _keyword.kwlist)
    ['except']
    """
    if not n > 0:
        raise ValueError('n must be > 0: %r' % (n,))
    if not 0.0 <= cutoff <= 1.0:
        raise ValueError('cutoff must be in [0.0, 1.0]: %r' % (cutoff,))
    result = []
    s = SequenceMatcher()
    s.set_seq2(word)
    for x in possibilities:
        s.set_seq1(x)
        if s.real_quick_ratio() >= cutoff:
            if s.quick_ratio() >= cutoff:
                if s.ratio() >= cutoff:
                    result.append((s.ratio(), x))

    result = _nlargest(n, result)
    return [x for score, x in result]


def _count_leading(line, ch):
    """
    Return number of `ch` characters at the start of `line`.

    Example:

    >>> _count_leading('   abc', ' ')
    3
    """
    i, n = 0, len(line)
    while i < n:
        if line[i] == ch:
            i += 1

    return i


class Differ:
    r"""'\n    Differ is a class for comparing sequences of lines of text, and\n    producing human-readable differences or deltas.  Differ uses\n    SequenceMatcher both to compare sequences of lines, and to compare\n    sequences of characters within similar (near-matching) lines.\n\n    Each line of a Differ delta begins with a two-letter code:\n\n        \'- \'    line unique to sequence 1\n        \'+ \'    line unique to sequence 2\n        \'  \'    line common to both sequences\n        \'? \'    line not present in either input sequence\n\n    Lines beginning with \'? \' attempt to guide the eye to intraline\n    differences, and were not present in either input sequence.  These lines\n    can be confusing if the sequences contain tab characters.\n\n    Note that Differ makes no claim to produce a *minimal* diff.  To the\n    contrary, minimal diffs are often counter-intuitive, because they synch\n    up anywhere possible, sometimes accidental matches 100 pages apart.\n    Restricting synch points to contiguous matches preserves some notion of\n    locality, at the occasional cost of producing a longer diff.\n\n    Example: Comparing two texts.\n\n    First we set up the texts, sequences of individual single-line strings\n    ending with newlines (such sequences can also be obtained from the\n    `readlines()` method of file-like objects):\n\n    >>> text1 = \'\'\'  1. Beautiful is better than ugly.\n    ...   2. Explicit is better than implicit.\n    ...   3. Simple is better than complex.\n    ...   4. Complex is better than complicated.\n    ... \'\'\'.splitlines(keepends=True)\n    >>> len(text1)\n    4\n    >>> text1[0][-1]\n    \'\\n\'\n    >>> text2 = \'\'\'  1. Beautiful is better than ugly.\n    ...   3.   Simple is better than complex.\n    ...   4. Complicated is better than complex.\n    ...   5. Flat is better than nested.\n    ... \'\'\'.splitlines(keepends=True)\n\n    Next we instantiate a Differ object:\n\n    >>> d = Differ()\n\n    Note that when instantiating a Differ object we may pass functions to\n    filter out line and character \'junk\'.  See Differ.__init__ for details.\n\n    Finally, we compare the two:\n\n    >>> result = list(d.compare(text1, text2))\n\n    \'result\' is a list of strings, so let\'s pretty-print it:\n\n    >>> from pprint import pprint as _pprint\n    >>> _pprint(result)\n    [\'    1. Beautiful is better than ugly.\\n\',\n     \'-   2. Explicit is better than implicit.\\n\',\n     \'-   3. Simple is better than complex.\\n\',\n     \'+   3.   Simple is better than complex.\\n\',\n     \'?     ++\\n\',\n     \'-   4. Complex is better than complicated.\\n\',\n     \'?            ^                     ---- ^\\n\',\n     \'+   4. Complicated is better than complex.\\n\',\n     \'?           ++++ ^                      ^\\n\',\n     \'+   5. Flat is better than nested.\\n\']\n\n    As a single multi-line string it looks like this:\n\n    >>> print(\'\'.join(result), end="")\n        1. Beautiful is better than ugly.\n    -   2. Explicit is better than implicit.\n    -   3. Simple is better than complex.\n    +   3.   Simple is better than complex.\n    ?     ++\n    -   4. Complex is better than complicated.\n    ?            ^                     ---- ^\n    +   4. Complicated is better than complex.\n    ?           ++++ ^                      ^\n    +   5. Flat is better than nested.\n\n    Methods:\n\n    __init__(linejunk=None, charjunk=None)\n        Construct a text differencer, with optional filters.\n\n    compare(a, b)\n        Compare two sequences of lines; generate the resulting delta.\n    '"""

    def __init__(self, linejunk=None, charjunk=None):
        """
        Construct a text differencer, with optional filters.

        The two optional keyword parameters are for filter functions:

        - `linejunk`: A function that should accept a single string argument,
          and return true iff the string is junk. The module-level function
          `IS_LINE_JUNK` may be used to filter out lines without visible
          characters, except for at most one splat ('#').  It is recommended
          to leave linejunk None; the underlying SequenceMatcher class has
          an adaptive notion of "noise" lines that's better than any static
          definition the author has ever been able to craft.

        - `charjunk`: A function that should accept a string of length 1. The
          module-level function `IS_CHARACTER_JUNK` may be used to filter out
          whitespace characters (a blank or tab; **note**: bad idea to include
          newline in this!).  Use of IS_CHARACTER_JUNK is recommended.
        """
        self.linejunk = linejunk
        self.charjunk = charjunk

    def compare(self, a, b):
        r"""
        Compare two sequences of lines; generate the resulting delta.

        Each sequence must contain individual single-line strings ending with
        newlines. Such sequences can be obtained from the `readlines()` method
        of file-like objects.  The delta generated also consists of newline-
        terminated strings, ready to be printed as-is via the writeline()
        method of a file-like object.

        Example:

        >>> print(''.join(Differ().compare('one\ntwo\nthree\n'.splitlines(True),
        ...                                'ore\ntree\nemu\n'.splitlines(True))),
        ...       end="")
        - one
        ?  ^
        + ore
        ?  ^
        - two
        - three
        ?  -
        + tree
        + emu
        """
        cruncher = SequenceMatcher(self.linejunk, a, b)
        for tag, alo, ahi, blo, bhi in cruncher.get_opcodes():
            if tag == 'replace':
                g = self._fancy_replace(a, alo, ahi, b, blo, bhi)
            elif tag == 'delete':
                g = self._dump('-', a, alo, ahi)
            elif tag == 'insert':
                g = self._dump('+', b, blo, bhi)
            elif tag == 'equal':
                g = self._dump(' ', a, alo, ahi)
            else:
                raise ValueError('unknown tag %r' % (tag,))
            yield from g

    def _dump(self, tag, x, lo, hi):
        """Generate comparison results for a same-tagged range."""
        for i in range(lo, hi):
            yield '%s %s' % (tag, x[i])

    def _plain_replace(self, a, alo, ahi, b, blo, bhi):
        if not (alo < ahi and blo < bhi):
            raise AssertionError
        if bhi - blo < ahi - alo:
            first = self._dump('+', b, blo, bhi)
            second = self._dump('-', a, alo, ahi)
        else:
            first = self._dump('-', a, alo, ahi)
            second = self._dump('+', b, blo, bhi)
        for g in (first, second):
            yield from g

    def _fancy_replace(self, a, alo, ahi, b, blo, bhi):
        r"""
        When replacing one block of lines with another, search the blocks
        for *similar* lines; the best-matching pair (if any) is used as a
        synch point, and intraline difference marking is done on the
        similar pair. Lots of work, but often worth it.

        Example:

        >>> d = Differ()
        >>> results = d._fancy_replace(['abcDefghiJkl\n'], 0, 1,
        ...                            ['abcdefGhijkl\n'], 0, 1)
        >>> print(''.join(results), end="")
        - abcDefghiJkl
        ?    ^  ^  ^
        + abcdefGhijkl
        ?    ^  ^  ^
        """
        best_ratio, cutoff = (0.74, 0.75)
        cruncher = SequenceMatcher(self.charjunk)
        eqi, eqj = (None, None)
        for j in range(blo, bhi):
            bj = b[j]
            cruncher.set_seq2(bj)
            for i in range(alo, ahi):
                ai = a[i]
                if ai == bj:
                    eqi, eqj = eqi is None and i, j
                else:
                    cruncher.set_seq1(ai)
                    if cruncher.real_quick_ratio() > best_ratio:
                        best_ratio, best_i, best_j = cruncher.quick_ratio() > best_ratio and cruncher.ratio() > best_ratio and cruncher.ratio(), i, j

        if best_ratio < cutoff:
            if eqi is None:
                yield from self._plain_replace(a, alo, ahi, b, blo, bhi)
                return
            best_i, best_j, best_ratio = eqi, eqj, 1.0
        else:
            eqi = None
        yield from self._fancy_helper(a, alo, best_i, b, blo, best_j)
        aelt, belt = a[best_i], b[best_j]
        if eqi is None:
            atags = btags = ''
            cruncher.set_seqs(aelt, belt)
            for tag, ai1, ai2, bj1, bj2 in cruncher.get_opcodes():
                la, lb = ai2 - ai1, bj2 - bj1
                if tag == 'replace':
                    atags += '^' * la
                    btags += '^' * lb
                elif tag == 'delete':
                    atags += '-' * la
                elif tag == 'insert':
                    btags += '+' * lb
                elif tag == 'equal':
                    atags += ' ' * la
                    btags += ' ' * lb
                else:
                    raise ValueError('unknown tag %r' % (tag,))

            yield from self._qformat(aelt, belt, atags, btags)
        else:
            yield '  ' + aelt
        yield from self._fancy_helper(a, best_i + 1, ahi, b, best_j + 1, bhi)

    def _fancy_helper(self, a, alo, ahi, b, blo, bhi):
        g = []
        if alo < ahi:
            if blo < bhi:
                g = self._fancy_replace(a, alo, ahi, b, blo, bhi)
            else:
                g = self._dump('-', a, alo, ahi)
        elif blo < bhi:
            g = self._dump('+', b, blo, bhi)
        else:
            yield from g

    def _qformat(self, aline, bline, atags, btags):
        r"""
        Format "?" output and deal with leading tabs.

        Example:

        >>> d = Differ()
        >>> results = d._qformat('\tabcDefghiJkl\n', '\tabcdefGhijkl\n',
        ...                      '  ^ ^  ^      ', '  ^ ^  ^      ')
        >>> for line in results: print(repr(line))
        ...
        '- \tabcDefghiJkl\n'
        '? \t ^ ^  ^\n'
        '+ \tabcdefGhijkl\n'
        '? \t ^ ^  ^\n'
        """
        common = min(_count_leading(aline, '\t'), _count_leading(bline, '\t'))
        common = min(common, _count_leading(atags[:common], ' '))
        common = min(common, _count_leading(btags[:common], ' '))
        atags = atags[common:].rstrip()
        btags = btags[common:].rstrip()
        yield '- ' + aline
        if atags:
            yield '? %s%s\n' % ('\t' * common, atags)
        yield '+ ' + bline
        if btags:
            yield '? %s%s\n' % ('\t' * common, btags)


import re

def IS_LINE_JUNK(line, pat=re.compile('\\s*(?:#\\s*)?$').match):
    r"""
    Return 1 for ignorable line: iff `line` is blank or contains a single '#'.

    Examples:

    >>> IS_LINE_JUNK('\n')
    True
    >>> IS_LINE_JUNK('  #   \n')
    True
    >>> IS_LINE_JUNK('hello\n')
    False
    """
    return pat(line) is not None


def IS_CHARACTER_JUNK(ch, ws=' \t'):
    r"""
    Return 1 for ignorable character: iff `ch` is a space or tab.

    Examples:

    >>> IS_CHARACTER_JUNK(' ')
    True
    >>> IS_CHARACTER_JUNK('\t')
    True
    >>> IS_CHARACTER_JUNK('\n')
    False
    >>> IS_CHARACTER_JUNK('x')
    False
    """
    return ch in ws


def _format_range_unified(start, stop):
    """Convert range to the "ed" format"""
    beginning = start + 1
    length = stop - start
    if length == 1:
        return '{}'.format(beginning)
    else:
        if not length:
            beginning -= 1
        return '{},{}'.format(beginning, length)


def unified_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n'):
    """
    Compare two sequences of lines; generate the delta as a unified diff.

    Unified diffs are a compact way of showing line changes and a few
    lines of context.  The number of context lines is set by 'n' which
    defaults to three.

    By default, the diff control lines (those with ---, +++, or @@) are
    created with a trailing newline.  This is helpful so that inputs
    created from file.readlines() result in diffs that are suitable for
    file.writelines() since both the inputs and outputs have trailing
    newlines.

    For inputs that do not have trailing newlines, set the lineterm
    argument to "" so that the output will be uniformly newline free.

    The unidiff format normally has a header for filenames and modification
    times.  Any or all of these may be specified using strings for
    'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
    The modification times are normally expressed in the ISO 8601 format.

    Example:

    >>> for line in unified_diff('one two three four'.split(),
    ...             'zero one tree four'.split(), 'Original', 'Current',
    ...             '2005-01-26 23:30:50', '2010-04-02 10:20:52',
    ...             lineterm=''):
    ...     print(line)                 # doctest: +NORMALIZE_WHITESPACE
    --- Original        2005-01-26 23:30:50
    +++ Current         2010-04-02 10:20:52
    @@ -1,4 +1,4 @@
    +zero
     one
    -two
    -three
    +tree
     four
    """
    _check_types(a, b, fromfile, tofile, fromfiledate, tofiledate, lineterm)
    started = False
    for group in SequenceMatcher(None, a, b).get_grouped_opcodes(n):
        if not started:
            started = True
            fromdate = '\t{}'.format(fromfiledate) if fromfiledate else ''
            todate = '\t{}'.format(tofiledate) if tofiledate else ''
            yield '--- {}{}{}'.format(fromfile, fromdate, lineterm)
            yield '+++ {}{}{}'.format(tofile, todate, lineterm)
        first, last = group[0], group[(-1)]
        file1_range = _format_range_unified(first[1], last[2])
        file2_range = _format_range_unified(first[3], last[4])
        yield '@@ -{} +{} @@{}'.format(file1_range, file2_range, lineterm)
        for tag, i1, i2, j1, j2 in group:
            if tag == 'equal':
                for line in a[i1:i2]:
                    yield ' ' + line

            else:
                if tag in frozenset(['replace', 'delete']):
                    for line in a[i1:i2]:
                        yield '-' + line

                if tag in frozenset(['insert', 'replace']):
                    for line in b[j1:j2]:
                        yield '+' + line


def _format_range_context(start, stop):
    """Convert range to the "ed" format"""
    beginning = start + 1
    length = stop - start
    if not length:
        beginning -= 1
    if length <= 1:
        return '{}'.format(beginning)
    else:
        return '{},{}'.format(beginning, beginning + length - 1)


def context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n'):
    r"""
    Compare two sequences of lines; generate the delta as a context diff.

    Context diffs are a compact way of showing line changes and a few
    lines of context.  The number of context lines is set by 'n' which
    defaults to three.

    By default, the diff control lines (those with *** or ---) are
    created with a trailing newline.  This is helpful so that inputs
    created from file.readlines() result in diffs that are suitable for
    file.writelines() since both the inputs and outputs have trailing
    newlines.

    For inputs that do not have trailing newlines, set the lineterm
    argument to "" so that the output will be uniformly newline free.

    The context diff format normally has a header for filenames and
    modification times.  Any or all of these may be specified using
    strings for 'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
    The modification times are normally expressed in the ISO 8601 format.
    If not specified, the strings default to blanks.

    Example:

    >>> print(''.join(context_diff('one\ntwo\nthree\nfour\n'.splitlines(True),
    ...       'zero\none\ntree\nfour\n'.splitlines(True), 'Original', 'Current')),
    ...       end="")
    *** Original
    --- Current
    ***************
    *** 1,4 ****
      one
    ! two
    ! three
      four
    --- 1,4 ----
    + zero
      one
    ! tree
      four
    """
    _check_types(a, b, fromfile, tofile, fromfiledate, tofiledate, lineterm)
    prefix = dict(insert='+ ', delete='- ', replace='! ', equal='  ')
    started = False
    for group in SequenceMatcher(None, a, b).get_grouped_opcodes(n):
        if not started:
            started = True
            fromdate = '\t{}'.format(fromfiledate) if fromfiledate else ''
            todate = '\t{}'.format(tofiledate) if tofiledate else ''
            yield '*** {}{}{}'.format(fromfile, fromdate, lineterm)
            yield '--- {}{}{}'.format(tofile, todate, lineterm)
        first, last = group[0], group[(-1)]
        yield '***************' + lineterm
        file1_range = _format_range_context(first[1], last[2])
        yield '*** {} ****{}'.format(file1_range, lineterm)
        if any(tag in frozenset(['replace', 'delete']) for tag, _, _, _, _ in group):
            for tag, i1, i2, _, _ in group:
                if tag != 'insert':
                    for line in a[i1:i2]:
                        yield prefix[tag] + line

        file2_range = _format_range_context(first[3], last[4])
        yield '--- {} ----{}'.format(file2_range, lineterm)
        if any(tag in frozenset(['insert', 'replace']) for tag, _, _, _, _ in group):
            for tag, _, _, j1, j2 in group:
                if tag != 'delete':
                    for line in b[j1:j2]:
                        yield prefix[tag] + line


def _check_types(a, b, *args):
    if a:
        if not isinstance(a[0], str):
            raise TypeError('lines to compare must be str, not %s (%r)' % (
             type(a[0]).__name__, a[0]))
        if b:
            if not isinstance(b[0], str):
                raise TypeError('lines to compare must be str, not %s (%r)' % (
                 type(b[0]).__name__, b[0]))
            for arg in args:
                if not isinstance(arg, str):
                    raise TypeError('all arguments must be str, not: %r' % (arg,))


def diff_bytes(dfunc, a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\n'):
    """
    Compare `a` and `b`, two sequences of lines represented as bytes rather
    than str. This is a wrapper for `dfunc`, which is typically either
    unified_diff() or context_diff(). Inputs are losslessly converted to
    strings so that `dfunc` only has to worry about strings, and encoded
    back to bytes on return. This is necessary to compare files with
    unknown or inconsistent encoding. All other inputs (except `n`) must be
    bytes rather than str.
    """

    def decode(s):
        try:
            return s.decode('ascii', 'surrogateescape')
        except AttributeError as err:
            try:
                msg = 'all arguments must be bytes, not %s (%r)' % (
                 type(s).__name__, s)
                raise TypeError(msg) from err
            finally:
                err = None
                del err

    a = list(map(decode, a))
    b = list(map(decode, b))
    fromfile = decode(fromfile)
    tofile = decode(tofile)
    fromfiledate = decode(fromfiledate)
    tofiledate = decode(tofiledate)
    lineterm = decode(lineterm)
    lines = dfunc(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm)
    for line in lines:
        yield line.encode('ascii', 'surrogateescape')


def ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK):
    r"""
    Compare `a` and `b` (lists of strings); return a `Differ`-style delta.

    Optional keyword parameters `linejunk` and `charjunk` are for filter
    functions, or can be None:

    - linejunk: A function that should accept a single string argument and
      return true iff the string is junk.  The default is None, and is
      recommended; the underlying SequenceMatcher class has an adaptive
      notion of "noise" lines.

    - charjunk: A function that accepts a character (string of length
      1), and returns true iff the character is junk. The default is
      the module-level function IS_CHARACTER_JUNK, which filters out
      whitespace characters (a blank or tab; note: it's a bad idea to
      include newline in this!).

    Tools/scripts/ndiff.py is a command-line front-end to this function.

    Example:

    >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
    ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
    >>> print(''.join(diff), end="")
    - one
    ?  ^
    + ore
    ?  ^
    - two
    - three
    ?  -
    + tree
    + emu
    """
    return Differ(linejunk, charjunk).compare(a, b)


def _mdiff(fromlines, tolines, context=None, linejunk=None, charjunk=IS_CHARACTER_JUNK):
    r"""Returns generator yielding marked up from/to side by side differences.

    Arguments:
    fromlines -- list of text lines to compared to tolines
    tolines -- list of text lines to be compared to fromlines
    context -- number of context lines to display on each side of difference,
               if None, all from/to text lines will be generated.
    linejunk -- passed on to ndiff (see ndiff documentation)
    charjunk -- passed on to ndiff (see ndiff documentation)

    This function returns an iterator which returns a tuple:
    (from line tuple, to line tuple, boolean flag)

    from/to line tuple -- (line num, line text)
        line num -- integer or None (to indicate a context separation)
        line text -- original line text with following markers inserted:
            '\0+' -- marks start of added text
            '\0-' -- marks start of deleted text
            '\0^' -- marks start of changed text
            '\1' -- marks end of added/deleted/changed text

    boolean flag -- None indicates context separation, True indicates
        either "from" or "to" line contains a change, otherwise False.

    This function/iterator was originally developed to generate side by side
    file difference for making HTML pages (see HtmlDiff class for example
    usage).

    Note, this function utilizes the ndiff function to generate the side by
    side difference markup.  Optional ndiff arguments may be passed to this
    function and they in turn will be passed to ndiff.
    """
    import re
    change_re = re.compile('(\\++|\\-+|\\^+)')
    diff_lines_iterator = ndiff(fromlines, tolines, linejunk, charjunk)

    def _make_line(lines, format_key, side, num_lines=[
 0, 0]):
        """Returns line of text with user's change markup and line formatting.

        lines -- list of lines from the ndiff generator to produce a line of
                 text from.  When producing the line of text to return, the
                 lines used are removed from this list.
        format_key -- '+' return first line in list with "add" markup around
                          the entire line.
                      '-' return first line in list with "delete" markup around
                          the entire line.
                      '?' return first line in list with add/delete/change
                          intraline markup (indices obtained from second line)
                      None return first line in list with no markup
        side -- indice into the num_lines list (0=from,1=to)
        num_lines -- from/to current line number.  This is NOT intended to be a
                     passed parameter.  It is present as a keyword argument to
                     maintain memory of the current line numbers between calls
                     of this function.

        Note, this function is purposefully not defined at the module scope so
        that data it needs from its parent function (within whose context it
        is defined) does not need to be of module scope.
        """
        num_lines[side] += 1
        if format_key is None:
            return (num_lines[side], lines.pop(0)[2:])
        else:
            if format_key == '?':
                text, markers = lines.pop(0), lines.pop(0)
                sub_info = []

                def record_sub_info(match_object, sub_info=sub_info):
                    sub_info.append([match_object.group(1)[0], match_object.span()])
                    return match_object.group(1)

                change_re.sub(record_sub_info, markers)
                for key, (begin, end) in reversed(sub_info):
                    text = text[0:begin] + '\x00' + key + text[begin:end] + '\x01' + text[end:]

                text = text[2:]
            else:
                text = lines.pop(0)[2:]
                if not text:
                    text = ' '
                text = '\x00' + format_key + text + '\x01'
            return (
             num_lines[side], text)

    def _line_iterator():
        """Yields from/to lines of text with a change indication.

        This function is an iterator.  It itself pulls lines from a
        differencing iterator, processes them and yields them.  When it can
        it yields both a "from" and a "to" line, otherwise it will yield one
        or the other.  In addition to yielding the lines of from/to text, a
        boolean flag is yielded to indicate if the text line(s) have
        differences in them.

        Note, this function is purposefully not defined at the module scope so
        that data it needs from its parent function (within whose context it
        is defined) does not need to be of module scope.
        """
        lines = []
        num_blanks_pending, num_blanks_to_yield = (0, 0)
        while True:
            while 1:
                if len(lines) < 4:
                    lines.append(next(diff_lines_iterator, 'X'))

            s = ''.join([line[0] for line in lines])
            if s.startswith('X'):
                num_blanks_to_yield = num_blanks_pending
            elif s.startswith('-?+?'):
                yield (_make_line(lines, '?', 0), _make_line(lines, '?', 1), True)
                continue
            elif s.startswith('--++'):
                num_blanks_pending -= 1
                yield (_make_line(lines, '-', 0), None, True)
                continue
            elif s.startswith(('--?+', '--+', '- ')):
                from_line, to_line = _make_line(lines, '-', 0), None
                num_blanks_to_yield, num_blanks_pending = num_blanks_pending - 1, 0
            elif s.startswith('-+?'):
                yield (_make_line(lines, None, 0), _make_line(lines, '?', 1), True)
                continue
            elif s.startswith('-?+'):
                yield (_make_line(lines, '?', 0), _make_line(lines, None, 1), True)
                continue
            elif s.startswith('-'):
                num_blanks_pending -= 1
                yield (_make_line(lines, '-', 0), None, True)
                continue
            elif s.startswith('+--'):
                num_blanks_pending += 1
                yield (None, _make_line(lines, '+', 1), True)
                continue
            elif s.startswith(('+ ', '+-')):
                from_line, to_line = None, _make_line(lines, '+', 1)
                num_blanks_to_yield, num_blanks_pending = num_blanks_pending + 1, 0
            elif s.startswith('+'):
                num_blanks_pending += 1
                yield (None, _make_line(lines, '+', 1), True)
                continue
            elif s.startswith(' '):
                yield (_make_line(lines[:], None, 0), _make_line(lines, None, 1), False)
                continue
            while num_blanks_to_yield < 0:
                num_blanks_to_yield += 1
                yield (None, ('', '\n'), True)

            while num_blanks_to_yield > 0:
                num_blanks_to_yield -= 1
                yield (('', '\n'), None, True)

            if s.startswith('X'):
                return
            yield (from_line, to_line, True)

    def _line_pair_iterator():
        """Yields from/to lines of text with a change indication.

        This function is an iterator.  It itself pulls lines from the line
        iterator.  Its difference from that iterator is that this function
        always yields a pair of from/to text lines (with the change
        indication).  If necessary it will collect single from/to lines
        until it has a matching pair from/to pair to yield.

        Note, this function is purposefully not defined at the module scope so
        that data it needs from its parent function (within whose context it
        is defined) does not need to be of module scope.
        """
        line_iterator = _line_iterator()
        fromlines, tolines = [], []
        while True:
            while 1:
                if len(fromlines) == 0 or len(tolines) == 0:
                    try:
                        from_line, to_line, found_diff = next(line_iterator)
                    except StopIteration:
                        return
                    else:
                        if from_line is not None:
                            fromlines.append((from_line, found_diff))
                        if to_line is not None:
                            tolines.append((to_line, found_diff))

            from_line, fromDiff = fromlines.pop(0)
            to_line, to_diff = tolines.pop(0)
            yield (from_line, to_line, fromDiff or to_diff)

    line_pair_iterator = _line_pair_iterator()
    if context is None:
        yield from line_pair_iterator
    else:
        context += 1
        lines_to_write = 0
        while True:
            index, contextLines = 0, [None] * context
            found_diff = False
            while 1:
                if found_diff is False:
                    try:
                        from_line, to_line, found_diff = next(line_pair_iterator)
                    except StopIteration:
                        return
                    else:
                        i = index % context
                        contextLines[i] = (from_line, to_line, found_diff)
                        index += 1

            if index > context:
                yield (None, None, None)
                lines_to_write = context
            else:
                lines_to_write = index
                index = 0
            while lines_to_write:
                i = index % context
                index += 1
                yield contextLines[i]
                lines_to_write -= 1

            lines_to_write = context - 1
            try:
                while lines_to_write:
                    from_line, to_line, found_diff = next(line_pair_iterator)
                    if found_diff:
                        lines_to_write = context - 1
                    else:
                        lines_to_write -= 1
                    yield (
                     from_line, to_line, found_diff)

            except StopIteration:
                return


_file_template = '\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html>\n\n<head>\n    <meta http-equiv="Content-Type"\n          content="text/html; charset=%(charset)s" />\n    <title></title>\n    <style type="text/css">%(styles)s\n    </style>\n</head>\n\n<body>\n    %(table)s%(legend)s\n</body>\n\n</html>'
_styles = '\n        table.diff {font-family:Courier; border:medium;}\n        .diff_header {background-color:#e0e0e0}\n        td.diff_header {text-align:right}\n        .diff_next {background-color:#c0c0c0}\n        .diff_add {background-color:#aaffaa}\n        .diff_chg {background-color:#ffff77}\n        .diff_sub {background-color:#ffaaaa}'
_table_template = '\n    <table class="diff" id="difflib_chg_%(prefix)s_top"\n           cellspacing="0" cellpadding="0" rules="groups" >\n        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>\n        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>\n        %(header_row)s\n        <tbody>\n%(data_rows)s        </tbody>\n    </table>'
_legend = '\n    <table class="diff" summary="Legends">\n        <tr> <th colspan="2"> Legends </th> </tr>\n        <tr> <td> <table border="" summary="Colors">\n                      <tr><th> Colors </th> </tr>\n                      <tr><td class="diff_add">&nbsp;Added&nbsp;</td></tr>\n                      <tr><td class="diff_chg">Changed</td> </tr>\n                      <tr><td class="diff_sub">Deleted</td> </tr>\n                  </table></td>\n             <td> <table border="" summary="Links">\n                      <tr><th colspan="2"> Links </th> </tr>\n                      <tr><td>(f)irst change</td> </tr>\n                      <tr><td>(n)ext change</td> </tr>\n                      <tr><td>(t)op</td> </tr>\n                  </table></td> </tr>\n    </table>'

class HtmlDiff(object):
    r"""'For producing HTML side by side comparison with change highlights.\n\n    This class can be used to create an HTML table (or a complete HTML file\n    containing the table) showing a side by side, line by line comparison\n    of text with inter-line and intra-line change highlights.  The table can\n    be generated in either full or contextual difference mode.\n\n    The following methods are provided for HTML generation:\n\n    make_table -- generates HTML for a single side by side table\n    make_file -- generates complete HTML file with a single side by side table\n\n    See tools/scripts/diff.py for an example usage of this class.\n    '"""
    _file_template = _file_template
    _styles = _styles
    _table_template = _table_template
    _legend = _legend
    _default_prefix = 0

    def __init__(self, tabsize=8, wrapcolumn=None, linejunk=None, charjunk=IS_CHARACTER_JUNK):
        """HtmlDiff instance initializer

        Arguments:
        tabsize -- tab stop spacing, defaults to 8.
        wrapcolumn -- column number where lines are broken and wrapped,
            defaults to None where lines are not wrapped.
        linejunk,charjunk -- keyword arguments passed into ndiff() (used by
            HtmlDiff() to generate the side by side HTML differences).  See
            ndiff() documentation for argument default values and descriptions.
        """
        self._tabsize = tabsize
        self._wrapcolumn = wrapcolumn
        self._linejunk = linejunk
        self._charjunk = charjunk

    def make_file(self, fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5, *, charset='utf-8'):
        """Returns HTML file of side by side comparison with change highlights

        Arguments:
        fromlines -- list of "from" lines
        tolines -- list of "to" lines
        fromdesc -- "from" file column header string
        todesc -- "to" file column header string
        context -- set to True for contextual differences (defaults to False
            which shows full differences).
        numlines -- number of context lines.  When context is set True,
            controls number of lines displayed before and after the change.
            When context is False, controls the number of lines to place
            the "next" link anchors before the next change (so click of
            "next" link jumps to just before the change).
        charset -- charset of the HTML document
        """
        return (self._file_template % dict(styles=(self._styles),
          legend=(self._legend),
          table=self.make_table(fromlines, tolines, fromdesc, todesc, context=context,
          numlines=numlines),
          charset=charset)).encode(charset, 'xmlcharrefreplace').decode(charset)

    def _tab_newline_replace(self, fromlines, tolines):
        """Returns from/to line lists with tabs expanded and newlines removed.

        Instead of tab characters being replaced by the number of spaces
        needed to fill in to the next tab stop, this function will fill
        the space with tab characters.  This is done so that the difference
        algorithms can identify changes in a file when tabs are replaced by
        spaces and vice versa.  At the end of the HTML generation, the tab
        characters will be replaced with a nonbreakable space.
        """

        def expand_tabs(line):
            line = line.replace(' ', '\x00')
            line = line.expandtabs(self._tabsize)
            line = line.replace(' ', '\t')
            return line.replace('\x00', ' ').rstrip('\n')

        fromlines = [expand_tabs(line) for line in fromlines]
        tolines = [expand_tabs(line) for line in tolines]
        return (
         fromlines, tolines)

    def _split_line(self, data_list, line_num, text):
        """Builds list of text lines by splitting text lines at wrap point

        This function will determine if the input text line needs to be
        wrapped (split) into separate lines.  If so, the first wrap point
        will be determined and the first line appended to the output
        text line list.  This function is used recursively to handle
        the second part of the split line to further split it.
        """
        if not line_num:
            data_list.append((line_num, text))
            return
        size = len(text)
        max = self._wrapcolumn
        if size <= max or size - text.count('\x00') * 3 <= max:
            data_list.append((line_num, text))
            return
        i = 0
        n = 0
        mark = ''
        while n < max and i < size:
            if text[i] == '\x00':
                i += 1
                mark = text[i]
                i += 1
            elif text[i] == '\x01':
                i += 1
                mark = ''
            else:
                i += 1
                n += 1

        line1 = text[:i]
        line2 = text[i:]
        if mark:
            line1 = line1 + '\x01'
            line2 = '\x00' + mark + line2
        data_list.append((line_num, line1))
        self._split_line(data_list, '>', line2)

    def _line_wrapper(self, diffs):
        """Returns iterator that splits (wraps) mdiff text lines"""
        for fromdata, todata, flag in diffs:
            if flag is None:
                yield (
                 fromdata, todata, flag)
                continue
                (fromline, fromtext), (toline, totext) = fromdata, todata
                fromlist, tolist = [], []
                self._split_line(fromlist, fromline, fromtext)
                self._split_line(tolist, toline, totext)
                while fromlist or tolist:
                    if fromlist:
                        fromdata = fromlist.pop(0)
                    else:
                        fromdata = ('', ' ')
                    if tolist:
                        todata = tolist.pop(0)
                    else:
                        todata = ('', ' ')
                    yield (
                     fromdata, todata, flag)

    def _collect_lines(self, diffs):
        """Collects mdiff output into separate lists

        Before storing the mdiff from/to data into a list, it is converted
        into a single line of text with HTML markup.
        """
        fromlist, tolist, flaglist = [], [], []
        for fromdata, todata, flag in diffs:
            try:
                fromlist.append((self._format_line)(0, flag, *fromdata))
                tolist.append((self._format_line)(1, flag, *todata))
            except TypeError:
                fromlist.append(None)
                tolist.append(None)

            flaglist.append(flag)

        return (fromlist, tolist, flaglist)

    def _format_line(self, side, flag, linenum, text):
        """Returns HTML markup of "from" / "to" text lines

        side -- 0 or 1 indicating "from" or "to" text
        flag -- indicates if difference on line
        linenum -- line number (used for line number column)
        text -- line text to be marked up
        """
        try:
            linenum = '%d' % linenum
            id = ' id="%s%s"' % (self._prefix[side], linenum)
        except TypeError:
            id = ''

        text = text.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
        text = text.replace(' ', '&nbsp;').rstrip()
        return '<td class="diff_header"%s>%s</td><td nowrap="nowrap">%s</td>' % (
         id, linenum, text)

    def _make_prefix(self):
        """Create unique anchor prefixes"""
        fromprefix = 'from%d_' % HtmlDiff._default_prefix
        toprefix = 'to%d_' % HtmlDiff._default_prefix
        HtmlDiff._default_prefix += 1
        self._prefix = [
         fromprefix, toprefix]

    def _convert_flags(self, fromlist, tolist, flaglist, context, numlines):
        """Makes list of "next" links"""
        toprefix = self._prefix[1]
        next_id = [
         ''] * len(flaglist)
        next_href = [''] * len(flaglist)
        num_chg, in_change = (0, False)
        last = 0
        for i, flag in enumerate(flaglist):
            if flag:
                if not in_change:
                    in_change = True
                    last = i
                    i = max([0, i - numlines])
                    next_id[i] = ' id="difflib_chg_%s_%d"' % (toprefix, num_chg)
                    num_chg += 1
                    next_href[last] = '<a href="#difflib_chg_%s_%d">n</a>' % (
                     toprefix, num_chg)
                else:
                    in_change = False

        if not flaglist:
            flaglist = [
             False]
            next_id = ['']
            next_href = ['']
            last = 0
            if context:
                fromlist = [
                 '<td></td><td>&nbsp;No Differences Found&nbsp;</td>']
                tolist = fromlist
            else:
                fromlist = tolist = [
                 '<td></td><td>&nbsp;Empty File&nbsp;</td>']
        if not flaglist[0]:
            next_href[0] = '<a href="#difflib_chg_%s_0">f</a>' % toprefix
        next_href[last] = '<a href="#difflib_chg_%s_top">t</a>' % toprefix
        return (
         fromlist, tolist, flaglist, next_href, next_id)

    def make_table(self, fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5):
        """Returns HTML table of side by side comparison with change highlights

        Arguments:
        fromlines -- list of "from" lines
        tolines -- list of "to" lines
        fromdesc -- "from" file column header string
        todesc -- "to" file column header string
        context -- set to True for contextual differences (defaults to False
            which shows full differences).
        numlines -- number of context lines.  When context is set True,
            controls number of lines displayed before and after the change.
            When context is False, controls the number of lines to place
            the "next" link anchors before the next change (so click of
            "next" link jumps to just before the change).
        """
        self._make_prefix()
        fromlines, tolines = self._tab_newline_replace(fromlines, tolines)
        if context:
            context_lines = numlines
        else:
            context_lines = None
        diffs = _mdiff(fromlines, tolines, context_lines, linejunk=(self._linejunk), charjunk=(self._charjunk))
        if self._wrapcolumn:
            diffs = self._line_wrapper(diffs)
        fromlist, tolist, flaglist = self._collect_lines(diffs)
        fromlist, tolist, flaglist, next_href, next_id = self._convert_flags(fromlist, tolist, flaglist, context, numlines)
        s = []
        fmt = '            <tr><td class="diff_next"%s>%s</td>%s<td class="diff_next">%s</td>%s</tr>\n'
        for i in range(len(flaglist)):
            if flaglist[i] is None:
                if i > 0:
                    s.append('        </tbody>        \n        <tbody>\n')
                else:
                    s.append(fmt % (next_id[i], next_href[i], fromlist[i],
                     next_href[i], tolist[i]))

        if fromdesc or todesc:
            header_row = '<thead><tr>%s%s%s%s</tr></thead>' % (
             '<th class="diff_next"><br /></th>',
             '<th colspan="2" class="diff_header">%s</th>' % fromdesc,
             '<th class="diff_next"><br /></th>',
             '<th colspan="2" class="diff_header">%s</th>' % todesc)
        else:
            header_row = ''
        table = self._table_template % dict(data_rows=(''.join(s)),
          header_row=header_row,
          prefix=(self._prefix[1]))
        return table.replace('\x00+', '<span class="diff_add">').replace('\x00-', '<span class="diff_sub">').replace('\x00^', '<span class="diff_chg">').replace('\x01', '</span>').replace('\t', '&nbsp;')


del re

def restore(delta, which):
    r"""
    Generate one of the two sequences that generated a delta.

    Given a `delta` produced by `Differ.compare()` or `ndiff()`, extract
    lines originating from file 1 or 2 (parameter `which`), stripping off line
    prefixes.

    Examples:

    >>> diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
    ...              'ore\ntree\nemu\n'.splitlines(keepends=True))
    >>> diff = list(diff)
    >>> print(''.join(restore(diff, 1)), end="")
    one
    two
    three
    >>> print(''.join(restore(diff, 2)), end="")
    ore
    tree
    emu
    """
    try:
        tag = {1:'- ', 
         2:'+ '}[int(which)]
    except KeyError:
        raise ValueError('unknown delta choice (must be 1 or 2): %r' % which) from None

    prefixes = (
     '  ', tag)
    for line in delta:
        if line[:2] in prefixes:
            yield line[2:]


def _test():
    import doctest, difflib
    return doctest.testmod(difflib)


if __name__ == '__main__':
    _test()
# uncompyle6 version 3.3.5
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Mar  4 2019, 09:02:22) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)]
# Embedded file name: ctypes\_endian.py
import sys
from ctypes import *
_array_type = type(Array)

def _other_endian(typ):
    """Return the type with the 'other' byte order.  Simple types like
    c_int and so on already have __ctype_be__ and __ctype_le__
    attributes which contain the types, for more complicated types
    arrays and structures are supported.
    """
    if hasattr(typ, _OTHER_ENDIAN):
        return getattr(typ, _OTHER_ENDIAN)
    if isinstance(typ, _array_type):
        return _other_endian(typ._type_) * typ._length_
    if issubclass(typ, Structure):
        return typ
    raise TypeError('This type does not support other endian: %s' % typ)


class _swapped_meta(type(Structure)):

    def __setattr__(self, attrname, value):
        if attrname == '_fields_':
            fields = []
            for desc in value:
                name = desc[0]
                typ = desc[1]
                rest = desc[2:]
                fields.append((name, _other_endian(typ)) + rest)

            value = fields
        super().__setattr__(attrname, value)


if sys.byteorder == 'little':
    _OTHER_ENDIAN = '__ctype_be__'
    LittleEndianStructure = Structure

    class BigEndianStructure(Structure, metaclass=_swapped_meta):
        """'Structure with big endian byte order'"""
        __slots__ = ()
        _swappedbytes_ = None


elif sys.byteorder == 'big':
    _OTHER_ENDIAN = '__ctype_le__'
    BigEndianStructure = Structure

    class LittleEndianStructure(Structure, metaclass=_swapped_meta):
        """'Structure with little endian byte order'"""
        __slots__ = ()
        _swappedbytes_ = None


else:
    raise RuntimeError('Invalid byteorder')
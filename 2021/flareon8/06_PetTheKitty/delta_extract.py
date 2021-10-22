
from ctypes import (windll, wintypes, c_uint64, c_uint32, cast, POINTER, Union, c_ubyte,
                    LittleEndianStructure, byref, c_size_t)
import zlib


# types and flags
DELTA_FLAG_TYPE             = c_uint64
DELTA_FLAG_NONE             = 0x00000000
DELTA_APPLY_FLAG_ALLOW_PA19 = 0x00000001


# structures
class DELTA_INPUT(LittleEndianStructure):
    class U1(Union):
        _fields_ = [('lpcStart', wintypes.LPVOID),
                    ('lpStart', wintypes.LPVOID)]
    _anonymous_ = ('u1',)
    _fields_ = [('u1', U1),
                ('uSize', c_size_t),
                ('Editable', wintypes.BOOL)]


class DELTA_OUTPUT(LittleEndianStructure):
    _fields_ = [('lpStart', wintypes.LPVOID),
                ('uSize', c_size_t)]

'''
typedef struct _DELTA_HEADER_INFO
{
    DELTA_FILE_TYPE FileTypeSet;
    DELTA_FILE_TYPE FileType;
    DELTA_FLAG_TYPE Flags;
    SIZE_T  TargetSize;
    FILETIME TargetFileTime;
    ALG_ID TargetHashAlgId;
    DELTA_HASH TargetHash;
} DELTA_HEADER_INFO;
'''

class DELTA_HEADER_INFO(LittleEndianStructure):
    _fields_ = [('FileTypeSet', c_uint64),
                ('FileType', c_uint64),
                ('Flags', c_uint64),
                ('TargetSize', c_size_t),
                ('TargetFileTime', wintypes.FILETIME),
                ('TargetHashAlgId', c_uint32),
                ('TargetHash', c_size_t),
                ('Reserved1', c_size_t),
                ('Reserved2', c_size_t),
                ]


# functions
ApplyDeltaB = windll.msdelta.ApplyDeltaB
ApplyDeltaB.argtypes = [DELTA_FLAG_TYPE, DELTA_INPUT, DELTA_INPUT,
                        POINTER(DELTA_OUTPUT)]
ApplyDeltaB.rettype = wintypes.BOOL

DeltaFree = windll.msdelta.DeltaFree
DeltaFree.argtypes = [wintypes.LPVOID]
DeltaFree.rettype = wintypes.BOOL

gle = windll.kernel32.GetLastError

GetDeltaInfoB = windll.msdelta.GetDeltaInfoB
GetDeltaInfoB.argtypes = [DELTA_INPUT, POINTER(DELTA_HEADER_INFO)]
GetDeltaInfoB.rettype = wintypes.BOOL


def apply_patchfile_to_buffer(buf, buflen, patchpath, legacy):
    with open(patchpath, 'rb') as patch:
        patch_contents = patch.read()

    # some patches (Windows Update MSU) come with a CRC32 prepended to the file
    # if the file doesn't start with the signature (PA) then check it
    if patch_contents[:2] != b"PA":
        paoff = patch_contents.find(b"PA")
        if paoff != 4:
            raise Exception("Patch is invalid")
        crc = int.from_bytes(patch_contents[:4], 'little')
        patch_contents = patch_contents[4:]
        if zlib.crc32(patch_contents) != crc:
            raise Exception("CRC32 check failed. Patch corrupted or invalid")

    applyflags = DELTA_APPLY_FLAG_ALLOW_PA19 if legacy else DELTA_FLAG_NONE

    dd = DELTA_INPUT()
    ds = DELTA_INPUT()
    dout = DELTA_OUTPUT()
    dhout = DELTA_HEADER_INFO()

    ds.lpcStart = buf
    ds.uSize = buflen
    ds.Editable = False

    dd.lpcStart = cast(patch_contents, wintypes.LPVOID)
    dd.uSize = len(patch_contents)
    dd.Editable = False

    
    
    status = GetDeltaInfoB(dd, byref(dhout))
    
    
#     print(hex(dhout.FileTypeSet)) ## 1 -> raw
#     print(hex(dhout.FileType)) ## 1
#     print(hex(dhout.Flags)) ## 0 -> DELTA_FLAG_NONE 
#     print(hex(dhout.TargetSize)) ## 0x15f200
    
#     print(hex(dhout.TargetFileTime.dwHighDateTime))
#     print(hex(dhout.TargetFileTime.dwLowDateTime))

# # Note: 0 = No signature is not supported for this call and will cause MSDelta to return a hash value of all 0s.
#     print(hex(dhout.TargetHashAlgId))
#     print(hex(dhout.TargetHash))
#     print(hex(dhout.Reserved1))
#     print(hex(dhout.Reserved2))
    
    status = ApplyDeltaB(applyflags, ds, dd, byref(dout))
    if status == 0:
        raise Exception("Patch {} failed with error {}".format(patchpath, gle()))

    return (dout.lpStart, dout.uSize)


if __name__ == '__main__':
    import sys
    import base64
    import hashlib
    import argparse

    ap = argparse.ArgumentParser()
    mode = ap.add_mutually_exclusive_group(required=True)
    output = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("-i", "--input-file",
                      help="File to patch (forward or reverse)")
    mode.add_argument("-n", "--null", action="store_true", default=False,
                      help="Create the output file from a null diff "
                           "(null diff must be the first one specified)")
    output.add_argument("-o", "--output-file",
                        help="Destination to write patched file to")
    output.add_argument("-d", "--dry-run", action="store_true",
                        help="Don't write patch, just see if it would patch"
                             "correctly and get the resulting hash")
    ap.add_argument("-l", "--legacy", action='store_true', default=False,
                    help="Let the API use the PA19 legacy API (if required)")
    ap.add_argument("patches", nargs='+', help="Patches to apply")
    args = ap.parse_args()

    if not args.dry_run and not args.output_file:
        print("Either specify -d or -o", file=sys.stderr)
        ap.print_help()
        sys.exit(1)

    if args.null:
        inbuf = b""
    else:
        with open(args.input_file, 'rb') as r:
            inbuf = r.read()

    buf = cast(inbuf, wintypes.LPVOID)
    n = len(inbuf)
    to_free = []
    try:
        for patch in args.patches:
            buf, n = apply_patchfile_to_buffer(buf, n, patch, args.legacy)
            to_free.append(buf)

        outbuf = bytes((c_ubyte*n).from_address(buf))
        if not args.dry_run:
            with open(args.output_file, 'wb') as w:
                w.write(outbuf)
    finally:
        for buf in to_free:
            DeltaFree(buf)

    finalhash = hashlib.sha256(outbuf)
    print("Applied {} patch{} successfully"
          .format(len(args.patches), "es" if len(args.patches) > 1 else ""))
    print("Final hash: {}"
          .format(base64.b64encode(finalhash.digest()).decode()))
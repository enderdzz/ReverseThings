
from itertools import cycle
from ctypes import wintypes, cast, c_ubyte
import delta_extract
import struct
import sys
import re

patch_feature = b"PA30"
header = b"<4sII"
header_sz = 12

# with open('raw1.bin', 'rb') as f:
#     c = f.read()

def decrypt(cmd):
    return bytes([i^j for i,j in zip(cmd, cycle(b'meoow'))])

def extract_patch(filename):
    subname = filename.split('.')[0]
    with open(filename, 'rb') as f:
        c = f.read()

    ind = [m.start() for m in re.finditer(patch_feature, c)]
    with open('./raw1.png', 'rb') as r:
        inbuf = r.read()
    n = len(inbuf)
    index = 0
    for i in ind:
        offset = i - header_sz
        index += 1
        magic, ori_size, size = struct.unpack(header, c[offset : offset + header_sz])
        
        patchpath = subname + '_' + str(index)
        with open(patchpath, 'wb') as f:
            f.write(c[offset + header_sz : offset + header_sz + size])
        
        buf = cast(inbuf, wintypes.LPVOID)
        buf, n = delta_extract.apply_patchfile_to_buffer(buf, n, patchpath, None)
        outbuf = bytes((c_ubyte*n).from_address(buf))

        sys.stdout.buffer.write(decrypt(outbuf[:ori_size]))
        delta_extract.DeltaFree(buf)

extract_patch("S2/s2_144.bin")
print("=======================================================")
extract_patch("S2/s2_139.bin")

# with open('139-1.patch', 'rb') as f:
#     c = bytearray(f.read())
# print(decrypt(c[:0x8b]))
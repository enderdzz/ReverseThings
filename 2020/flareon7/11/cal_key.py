from Crypto.Util.number import *
import sys
def calc(N, root, d, name):
    with open(d, 'rb') as f:
        c = f.read()
    # print(hex(len(c)))
    # print(c[-128:])
    ct = bytes_to_long(c[-128:])
    dd = 0x10001
    key = long_to_bytes(pow(ct, dd, N))[-(0x10+8):-8]
    # print(key)
    with open(root+"_keys/" + name[:-3]+"key", 'wb') as f:
        f.write(key)

N = b"\xC3\xDA\x26\x3D\xF1\x72\x29\x33\x73\xB0\x43\x1E\xE0\x0B\xAC\x4C\x3D\xB7\x23\xBE\xE2\xD9\xCC\xC0\xA7\xEF\x8D\x03\x68\xC3\x3C\x57\x7D\xF7\xE6\x4F\x09\x50\x34\x37\xE9\x17\x85\x33\xC9\xF3\xB4\xD4\xEE\xBD\x7F\xE1\x07\x5E\x2E\x55\x39\x39\xD4\x3C\x25\xEB\x8A\x89\xA5\xFD\x7A\xD5\xF8\xA5\x2C\x20\x71\x3A\xE8\x78\xCF\x2B\x1F\x32\x2A\xCF\xE8\xB7\xC5\x5D\xAD\x60\xB3\x52\x06\x14\x19\xFA\x71\x3C\x90\x3D\x9E\xFC\x36\xBA\xF9\x51\x85\x88\x0D\x03\xEC\x16\x5A\x51\x18\x6C\xF1\xC3\x23\xBC\x58\xC4\x0B\x85\xFC\xBC\x7F\xA1\x62\xAD"
N = bytes_to_long(N)


# import os
# for root,dirs,files in os.walk(sys.argv[1]):
#     print(files)
#     for _f in files:
#         calc(N, sys.argv[1], sys.argv[1]+'/'+_f, _f)

with open('C_DLL/RowmapGuiprotocol_export.dll', 'rb') as f:
        rowman = f.read()
dat = rowman[0x10400:0x10400+0xe0]
ct = bytes_to_long(dat[-128:])
dd = 0x10001
key = long_to_bytes(pow(ct, dd, N))
print(key[-(0x10+8):-8])
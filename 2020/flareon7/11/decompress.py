from aplib import *
from struct import unpack
import sys

def dec(root, path, name):
    with open(path, 'rb') as f:
        c = f.read()
    _, header_size, code_size, _, _ = unpack("<IIIII", c[:0x14])
    assert len(c) == header_size + code_size
    ans = decompress(c[header_size:])

    print(path, ans[:2])
    with open(root+"_dll/"+name[:-10]+'dat', 'wb') as f:
        c = f.write(ans)

# import os
# for root,dirs,files in os.walk(sys.argv[1]):
#     print(files)
#     for _f in files:
#         dec(sys.argv[1][:-11], sys.argv[1]+'/'+_f, _f)
        
with open('new.dll', 'rb') as f:
    n = f.read()
with open('publickey1.dat', 'rb') as f:
    pk = f.read()
print(n[0x13800:0x13800+0x110])
assert pk == n[0x13800:0x13800+0x110]


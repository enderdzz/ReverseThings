
def mem(offset, size):
    return bytearray(vm[offset : offset+size])

def u4(offset, size):
    return unpack("<I", bytearray(vm[offset : offset+size]))[0]

from struct import *
with open('Languagetheme_dll/MonitornewWarningmap_export.dat', 'rb') as f:
    vm = f.read()

size = unpack("<h", vm[:2])[0]
for i in range(size):
    v5 = u4((2+i*6)*4, 4)
    print(i, "case:", hex(v5), hex(0xb961999e ^ v5))
    
    if (vm[(3+i*6)*4] & 1) != 0:
        print(vm[(2+i*6)*4 + u4((4+i*6)*4, 4):])
        key = vm[6*i+2] + vm[6*i+4]
        if vm[6*i+6]:
            v7 = v5 + vm[6*i+6]
        else:
            v7 = 0
    else:
        key = vm[6*i+4]
        v7 = vm[6*i+6]
    
    print("arg:", key, hex(key), v7, 0, 0)
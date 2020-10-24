
from struct import *
def _rol(val, bits, bit_size):
    return (val << bits % bit_size) & (2 ** bit_size - 1) | \
           ((val & (2 ** bit_size - 1)) >> (bit_size - (bits % bit_size)))
def _ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))
ror4 = lambda val, bits: _ror(val, bits, 32)
rol4 = lambda val, bits: _rol(val, bits, 32)


def xor_dec(c, size, key, p):
    v5 = 0
    v6 = 0
    ans = b''
    index = 0
    for i in range(size>>2, 0, -1):
        v = unpack("<I", c[index:index+4])[0]
        next_v = unpack("<I", c[index+4:index+8])[0]
        if v == 0 and i > 1 and next_v == 0:
            break
        v11 = v ^ v6 ^ key
        #print(hex(v11))
        v6 = (v5<<2)&0xff
        v5 ^= 1
        o = v6
        v6 = v
        v12 = 0
        c[index:index+4] = pack("<I", rol4(v11, o))
        ans += c[index:index+4]
        index += 4
    
    with open("plain.txt", 'wb') as f:
        f.write(ans)
    print("ans len:", len(ans))
    return ans

def mem(offset, size):
    return bytearray(con[offset : offset+size])

def u4(offset, size):
    return unpack("<I", bytearray(con[offset : offset+size]))[0]

import sys
# with open("C_DLL/WordlibSystemser_export.dll", 'rb') as f:
#     con =f.read()
#path = "C_DLL/WebmodeThemearchive_export.dll"
with open(sys.argv[1], 'rb') as f:
    con = f.read()
#v6 = con[u4(0x3c+0x18+0xf0,4):]


#key = 0xE7019EF0
#wordlib
timestamp = 0x5e613172
VA = 0x12000
size_of_data = 0x400

# webmode
# timestamp = 0x5e613175
# VA = 0x8000
# size_of_data = 0x400

# rowmap
timestamp = 0x5e61317a
VA = 0xf000
size_of_data = 0xc00


# soflogic
timestamp = 0x5e61317b
VA = 0x19000
size_of_data = 0xc00

#protocolmagic
timestamp = 0x5e61317d
VA = 0x7000
size_of_data = 0xa00

key = (timestamp ^ 0xB961999E) ^ (VA+size_of_data)
print(hex(key))

#m = mem(0x12400, 0x1000)

file_offset = int(sys.argv[2], 16)
file_size = 0x1000

m = mem(file_offset, 0x1000)
print(m)
ans = xor_dec(m, 0x1000, key, 1)

def patch(offset, ans):
    with open(sys.argv[1], 'wb') as f:
        f.write(con[:offset]+ans+con[offset+len(ans):])

#patch(file_offset, ans)
key = ror4(key, 1) # here is i

from serpent import *
from struct import *

def _rol(val, bits, bit_size):
    return (val << bits % bit_size) & (2 ** bit_size - 1) | ((val & (2 ** bit_size - 1)) >> (bit_size - (bits % bit_size)))
def _ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))
ror4 = lambda val, bits: _ror(val, bits, 32)
rol4 = lambda val, bits: _rol(val, bits, 32)

with open('DiMap_export.bin', 'rb') as f:
    c = f.read()

l = [i for i in unpack("<"+'I'*(len(c)//4), c)]

key = unpack("<II", "\xFA{0\xFBN{pU")[0]

def f43(ct, key):
    flag = 0
    v4 = 0
    cnt = len(ct)
    ct = [0] + ct
    
    for i in range(1, len(ct)):
        v4 = v4 ^ key ^ ror4(ct[i], 4*flag)
        flag ^= 1
        ct[i-1] = v4
    print(ct)
    
def rev_f43(ct, key):
    flag = 0
    v4 = 0
    ans = ''
    for i in range(0, len(ct)-1):
        tmp = ct[i]
        t = rol4(ct[i]^key^v4, 4*flag)
        flag ^= 1
        ans += pack("<I", t)
        
        v4 = ct[i]
    return ans

#f43([1234, 5678, 8976], key)
ans = rev_f43(l, key)
serpent_key = 'GSPyrv3C79ZbR0k1'
ans = serpent_cbc_decrypt(serpent_key, ans, iv='\x00'*16)
with open('flag.zip', 'wb') as f:
    f.write(ans)

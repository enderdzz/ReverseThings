from Crypto.Cipher import ARC4

with open('evil_clean.exe', 'rb') as f:
    c = f.read()

pick = lambda offset, len: c[offset:offset+len]

k1 = pick(0x2ce3c8, 16)
k2 = pick(0x2ce390, 16)

c1 = pick(0x1b5b30, 0x118836)
c2 = pick(0x2ce3a0, 37) # b'N3ver_G0nNa_g1ve_y0u_Up@flare-on.com\x00'

# cipher = ARC4.new(k1)
# data = cipher.decrypt(c1)
# with open("output.bmp", "wb") as f:
#     f.write(data)

def dyn_get(): # here is another way!
    generate_key    = ida_idd.Appcall.typedobj("unsigned int __cdecl generate_key_C869F0(unsigned __int8 *str, unsigned int a2, unsigned __int8 *a3);")
    generate_key.ea = ida_name.get_name_ea(0, "generate_key_C869F0")
    generate_key(0x72178c, 3, 0x72177c)

    ida_bytes.get_bytes(0x72177c, 4)

def gent():
    tbl = []
    for j in range(256):
        for i in range(8):
            if (j & 1) != 0 :
                v2 = 0
            else:
                v2 = (0xE5513017 + 0x8675309) & 0xffffffff
            j = v2 ^ (j >> 1)
        tbl.append(j ^ 0xFF000000)
    
    return tbl

from struct import pack

'''
we can dynamically solve this by dyn_get() without code transcription.
'''
def generate():
    
    tbl = gent()
    
    namelist  = [b"L0ve\x00", b"s3cret\x00", b"5Ex\x00", b"g0d\x00"]
    whole_key = b""
    for name in namelist:
        key = 0
        for i in range(len(name)):
            key = tbl[name[i] ^ (key & 0xff)] ^ (key >> 8)
        
        whole_key += pack("<I", key)[::-1]

    return whole_key

k3 = generate()# k3 is generated. L0ve s3cret 5Ex g0d
c3 = pick(0x2ce368, 39)

print(c3)
cipher = ARC4.new(k3)
data = cipher.decrypt(c3)
print(data)
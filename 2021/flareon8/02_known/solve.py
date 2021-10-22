import os

def ROL(data, shift, size=32):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)
     
 
def ROR(data, shift, size=32):
    shift %= size
    body = data >> shift
    remains = (data << (size - shift)) - (body << size)
    return (body + remains)

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def decrypt(enc, k):
    plain = []
    for i in range(len(enc)):
        plain.append( (rol(enc[i]^k[i], i, 8) - i + 256) & 0xff)
    return bytes(plain)

def retrieve_key(ori, enc):
    key = []
    for i in range(8):
        key.append( ror(i+ori[i], i, 8) ^ enc[i] )
    return bytes(key)

png_header = bytes([137, 80, 78, 71, 13, 10, 26, 10])

with open('Files/capa.png.encrypted', 'rb') as f:
     content = f.read()
with open('Files/commandovm.gif.encrypted', 'rb') as f:
    enc_header2 = f.read()[:8]
enc_header = content[:8]
k = retrieve_key(png_header, enc_header)

## verify the key
print(decrypt(enc_header2, k))

for root,dirs,names in os.walk("Files/"):
    for filename in names:
        print(root,filename[:-10])

        with open(root+filename, 'rb') as f:
            content = f.read()
            
        plain = bytearray()
        for i in range(0, len(content), 8):
            plain += decrypt(content[i:i+8], k)
        
        with open("DecFiles/"+filename[:-10], 'wb') as f:
            f.write(plain)
    
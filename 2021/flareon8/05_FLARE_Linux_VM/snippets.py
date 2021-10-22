from itertools import cycle
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Cipher import ARC4 as rc4cipher

import os

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

xor_key = b"Reese's"
def xor_crypto(c, k):
    ans = ""
    for i in zip(c, cycle(k)):
        #print(i)
        ans += chr(i[0]^i[1])
    return ans

NUMBER1 = 2
NUMBER2 = 3
NUMBER3 = 37
def calc_crypto(c):
    ans = ""
    for i in range(len(c)):
        ans += chr(( c[i] + 27 + NUMBER1 * NUMBER2 - NUMBER3) & 0xff)
    return ans

rc4_key = "SREFBE"
def rc4_crypto(c, k):
        key = bytes(k, encoding='utf-8')
        enc = rc4cipher.new(key)
        res = enc.decrypt(c)
        return res

# CBC mode, 
IV = b'PIZZA' + b'\x00'*11
aes_key = b'Sheep should sleep in a shed15.2'
def aes_crypto(c, k, iv):
    cipher = AES.new(k, AES.MODE_CBC, iv=iv)
    plain = cipher.decrypt(c)
    return plain

# def rc4_crypto(txt, key):
#     a = [i for i in range(256)]
#     index = 0
#     for j in range(256):
#         index = (a[j] + index + key[j % len(key)]) % 256;
#         v6 = a[j]
#         a[j] = a[index]
#         a[index] = v6
#     v9 = 0
#     index = 0
#     v8 = 0
#     for k in range(1024):
#         v9 = (v9 + 1) % 256
#         index = (index + a[v9]) % 256
#         v5 = a[v9]
#         a[v9] = a[index]
#         a[index] = v5
#         v4 = a[(a[index] + a[v9]) % 256]
#         txt[k] ^= v4 ^ v8
#         result = v4
#         v8 = v4
#     return txt

# for root,dirs,names in os.walk("DecFiles/"):
#     for filename in names:
#         if filename.startswith("used."):
#             continue
#         print(filename)
        
#         with open(root+filename, 'rb') as f:
#             content = bytearray(f.read()).strip(b'\x00')
#         #plain = xor_crypto(content, xor_key)
#         #plain = calc_crypto(content)
#         #plain = rc4_crypto(content, rc4_key)
#         plain = aes_crypto(unhexlify(content), aes_key, IV)
#         print(plain)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]

for i in primes:
    for j in primes:
        print(i+j) # occur number should be exactly 4!!!!

hash_value = "b3c20caa9a1a82add9503e0eac43f741793d2031eb1c6e830274ed5ea36238bf"
import hashlib
for i in range(256):
    m = hashlib.sha256()
    # E4Q5d6f`s4ls5I
    m.update(b"E4Q5d6f`s4l"+bytes([i])+b"5I")
    print(chr(i), m.digest())

# with open('DecFiles/used.sausages.txt', 'rb') as f: # used. 2st (typo) char.
#     c = bytearray(f.read(100))
# for i in range(len(c)):
#     c[i] = rol(c[i], 1, 8)
# print(c)

# with open('DecFiles/used.spaghetti.txt', 'rb') as f: # used. nothing useful.
#    c = bytearray(f.read(100))
# for i in range(len(c)):
#     c[i] = ror(c[i], 7, 8)
# print(c)

# with open('DecFiles/used.strawberries.txt', 'rb') as f: # used. nothing useful.
#     c = bytearray(f.read(300))
# for i in range(len(c)):
#     c[i] = ror(c[i], 7, 8)    
# print(c)


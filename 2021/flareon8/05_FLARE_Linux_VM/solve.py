import os
key = b"A secret is no longer a secret once someone knows it"

def rc4_crypto(txt):
    a = [i for i in range(256)]
    index = 0
    for j in range(256):
        index = (a[j] + index + key[j % 52]) % 256;
        v6 = a[j]
        a[j] = a[index]
        a[index] = v6
    v9 = 0
    index = 0
    v8 = 0
    for k in range(1024):
        v9 = (v9 + 1) % 256
        index = (index + a[v9]) % 256
        v5 = a[v9]
        a[v9] = a[index]
        a[index] = v5
        v4 = a[(a[index] + a[v9]) % 256]
        txt[k] ^= v4 ^ v8
        result = v4
        v8 = v4
    return txt
        
for root,dirs,names in os.walk("Documents/"):
    for filename in names:
        print(filename)

        with open(root+filename, 'rb') as f:
            content = bytearray(f.read())
            #print(len(content))
        plain = rc4_crypto(content)
        
        with open("DecFiles/"+filename[:-7], 'wb') as f:
            f.write(plain)


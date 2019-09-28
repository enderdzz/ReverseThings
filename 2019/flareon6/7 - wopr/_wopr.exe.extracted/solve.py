import zlib
import sys
import os

num = 0
for file in os.listdir("."):
    if '.zlib' in file:
        with open(file, 'rb') as f:
            t = f.read()
        plaintext = zlib.decompress(t)
        n = 'DATA'
        if plaintext[:2] == 'MZ':
            n = 'EXE'
        name = n + str(num)
        num += 1
        with open(name, 'wb') as f:
            ##f.write('\x03\xf3\x0d\x0a\0\0\0\0')
            f.write(plaintext)


import zlib
import sys
import os

num = 0
for file in os.listdir("."):
    if file == 'c' or file == 'd':
        continue
    with open(file, 'rb') as f:
        plaintext = f.read()
    n = 'MISC'
    flag = False
    if plaintext[:2] == '\xe3\x00':
        n = 'PYC'
        flag = True
    name = n + str(num) + '.pyc'
    num += 1
    with open(name, 'wb') as f:
        if flag:
            f.write('\x42\x0d\x0d\x0a\0\0\0\0\0\0\0\0\0\0\0\0') # 420d 0d0a 0000 0000 0000 0000
        f.write(plaintext)


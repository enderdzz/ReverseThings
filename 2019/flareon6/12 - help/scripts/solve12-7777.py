import binascii
from pprint import pprint
traffic = []
with open('164.raw', 'rb') as f:
    command = f.read()

print hex(len(command))
key = [0x4a,0x1f,0x4b,0x1c,0xb0,0xd8,0x25,0xc7]

cmd = ''
for j in range(len(command)):
    cmd += chr(ord(command[j]) ^ key[j%8])

print hex(len(cmd))
with open('7777.bin', 'wb') as f:
    f.write(cmd)
with open('7777-164.bmp', 'wb') as f:
    f.write(cmd[4:])

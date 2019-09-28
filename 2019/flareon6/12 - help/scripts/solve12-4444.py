import binascii
from pprint import pprint
traffic = []
with open('4444.data', 'r') as f:
    for i in range(150):
        a = f.readline().strip('\n')
        if a != '':
            traffic.append(binascii.unhexlify(a))
            #print repr(a)

key = [0x5d,0xf3,0x4a,0x48,0x48,0x48,0xdd,0x23]
ans = []
for command in traffic:
    print len(command)
    cmd = ''
    for j in range(len(command)):
        cmd += chr(ord(command[j]) ^ key[j%8])
    ans.append(cmd)
pprint(ans)

#with open('4444.bin', 'wb') as f:
#    f.write(''.join(ans)[0x51f:])

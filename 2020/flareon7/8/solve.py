# idapython
# raw = get_bytes(here(), 0x10)
# print(''.join('\\x{:02x}'.format(ord(c)) for c in raw))

ct = b'\x4a\x82\x43\xab\x95\xed\x8f\x7e\x9c\xbc\xad\x84\x17\x91\x06\x15'
#cpu = b'cpufreq_'
fs = b'fs'
sig = b'Microsoft'
################### these values are wrong, I use gef-gdb on WSL to get correct values.
aux = b'\x70\xff\xff\xff\xff'*3
dirn = b'\0\0\0\0' 

ct1 = bytearray([i^ord('O') for i in ct])

summ = fs+sig+aux+dirn
for i in range(len(summ)):
    ct1[i%0xf] ^= summ[i]

print("ct1:", ct1)
#print("ct2:", ct2)

# https://stackoverflow.com/questions/49071746/how-to-get-the-size-of-the-vdso-on-a-linux-x86-64-system

# flag: c1ArF/P2CjiDXQIZ@flare-on.com
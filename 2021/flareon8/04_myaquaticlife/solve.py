from hashlib import md5

ans = b'6c5215b12a10e936f8de1e42083ba184'

v7C = b'PXopvMDFWEyEWBGgsuhn'
v74 = b'SLdkvnewauiHwdwAZ'
tbl = b'0123456789abcdef'
inp = bytearray(b'\x96%\xa4\xa9\xa3\x96\x9a\x90\x9f\xaf\xe58\xf9\x81\x9e\x16\xf9\xcb\xe4\xa4\x87\x8f\x8f\xba\xd2\x9d\xa7\xd1\xfc\xa3\xa8\x00') # the order of two xmm registers is improtant.

for i in range(31): # take care.
    inp[i] ^= v7C[i%len(v7C)]
    inp[i] = (inp[i] - v74[i % 0x11] + 0x100) & 0xff
inp = inp[:-1]
result = b''.join(bytes([tbl[i>>4], tbl[i&0xf]]) for i in md5(inp).digest())
assert(result == ans)
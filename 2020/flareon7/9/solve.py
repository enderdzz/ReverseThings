from hashlib import sha256
from Crypto.Cipher import Salsa20, ChaCha20

git = b'<g~{<it'
key2 = b'\x08\x67\x53\x09'
'''
# shift+f2 to start script command window, it's very convenient.

print("="*40)
decode_addr = 0x140001B54
for xref in XrefsTo(decode_addr, True):
  #print(hex(xref.frm))
  list = idaapi.get_arg_addrs(xref.frm) # I have found out that if in the disassembler you give the type to the function that is being called, then the ida python function will work as it should. https://reverseengineering.stackexchange.com/questions/25301/getting-function-arguments-in-ida
  if list != None:
    s = GetOpnd(list[0], 1)
    if s.startswith("qword"):
      raw = idaapi.get_fileregion_offset(int(s[6:],16))
      print(hex(raw), GetOpnd(list[1], 1))
    #print("found", GetOpnd(list[0], 1))
'''
offset = [
    ('0x173d0', '0x0D'),
    ('0x17318', '0x0F'),
    ('0x17470', '0x0D'),
    ('0x17328', '0x13'),
    ('0x17450', '0x0E'),
    ('0x173f0', '0x0F'),
    ('0x17340', '0x0E'),
    ('0x17308', '0x0F'),
    ('0x173e0', '0x0C'),
    ('0x17460', '0x10'),
    ('0x17388', '0x1c'),
    ('0x17300', '0x04'),
    ('0x173c0', '0x0f'),
    ('0x17418', '0x26'),
    ('0x17370', '0x12'),
    ('0x17350', '0x19'),
    ('0x173a8', '0x16'),
    ('0x17400', '0x12'),
]

def decode(ct, key, mod):
    return bytes([ct[i]^key[i%mod] for i in range(len(ct))])
    
def solve():
    with open("crackstaller.exe", 'rb') as f:
        content = bytearray(f.read())
    for i in offset:
        pt = decode(content[int(i[0], 16):int(i[0], 16)+int(i[1], 16)], git, 7)
        print(pt)
    
    # with open('dmp', 'wb') as f:
    #     f.write(decode(content[0x17480: 0x17480+0x1A600], key2, 4))
    
    # 36338 -> 3635C
    buf  = content[0x33d38:0x33d38+16]
    buf += content[0x33d48:0x33d48+16]
    buf += content[0x33d58:0x33d58+5]
    buf[0x46-0x38] = 0x58
    print(buf)
    with open("shellcode", 'wb') as f:
        content = f.write(buf)
    print('='*50)
    with open("payload.sys", 'rb') as f:
        content = f.read()
    n_offset = [('0x4a08', '0x0f'),
            ('0x4a40', '0x2e'),
            ('0x4a70', '0x07'),
            #('0x4a8c', '0x07'),
            ]
    for i in n_offset:
        pt = decode(content[int(i[0], 16):int(i[0], 16)+int(i[1], 16)], git, 7)
        print(pt)

    data = b'BBACABA'
    h = sha256()
    h.update(data)
    key = h.digest()
    
    ct = content[0x4a78:0x4a78+0x10]
    print(ct)
    #ct = bytes([ct[i]^i for i in range(len(ct))])
    cipher = ChaCha20.new(key=key, nonce=b'\0'*8)
    passwd = cipher.decrypt(ct)
    l = len(passwd)
    buf = [i for i in range(256)]
    v7 = 0
    v8 = 0
    v12 = 0
    for i in range(256):
        v14 = buf[i]
        v15 = v12 + 1
        v16 = passwd[v12]
        v12 = 0
        v7 = (v7 + buf[i] + v16) & 0xff
        buf[i] = buf[v7]
        buf[v7] = v14
        v17 = v8 + 1
        v8 = 0
        if v15 < l:
            v8 = v17
            v12 = v15
    print(len(buf), buf)

    with open("credHelper.dll", 'rb') as f:
        content = f.read()
    tbl = content[0x187f0:0x187f0+48]
    v4 = buf[0]
    v5 = 0
    v6 = buf[1]
    ans = []
    o = 2
    for i in range(45):
        v4 += 1
        v7 = buf[(v4+o)&0xff]
        v6 += v7
        v8 = buf[(v6+o)&0xff]
        buf[(v4+o)&0xff] = v8
        buf[(v6+o)&0xff] = v7
        ans.append(chr(tbl[v5] ^ buf[(v7+v8+o)&0xff]))
        v5 += 1
    
    print(''.join(ans))

solve()
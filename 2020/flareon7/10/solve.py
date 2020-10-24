from binascii import hexlify, unhexlify
from struct import unpack
#a = b'odhggjjcmhfmoipfifmfenbbbgpkpeoiaa'

#for i in range(0,len(a)//2):
#    print(i, hex((16*(a[i*2]-1)) |((a[i*2+1]-1)&0xf)))
    
def tran(a1,a2):
    return (a1 >> (a2 & 0x1F)) | (a1 << (-(a2 & 0x1F) & 0x1F))
def calc(mode, tup):
    v2 = (mode + tup[0]) & 0xffffffff
    v3 = tran(v2, tup[2]) & 0xffffffff
    res = (v3 ^ tup[1]) & 0xffffffff
    #print(hex(v2),hex(v3),hex(res))
    return res

ini = 0x674a1dea4b695809

buf = []

for i in range(16):
    _ = []
    print("+28:", hex(ini&((1<<32)-1)))
    _.append(ini&((1<<32)-1))
    print("+76:", hex((ini>>32)&((1<<32)-1)))
    _.append((ini>>32)&((1<<32)-1))
    cnt = 0
    for i in bin(ini):
        if i=='1': cnt+=1
    print("+164:", cnt//2) # +164
    _.append(cnt//2)
    buf.append(_)
    v6 = ini & 1
    ini >>=1
    if v6 == 1:
        v8 = 0x9E3779B9C6EF3720
        ini ^= v8

# inp = [0,0]
# inp[0] = 0x636c3377
# inp[1] = 0x5f456d30

def nom(inp):
    v6 = inp[0]
    mode = inp[1]
    for i in range(16):
        v9 = v6 ^ calc(mode, buf[i])
        v6 = mode
        mode = v9
        #print("v9:", hex(mode))

    #inp[0] = mode
    #inp[1] = v6
    #print("res0:", hex(inp[0]), "res1:",hex(inp[1]))
    
    r0 = hex(mode)[2:] 
    r1 = hex(v6)[2:]
    print(r0, r1)
    return unhexlify(r0.zfill(8))[::-1] + unhexlify(r1.zfill(8))[::-1]

with open('break', 'rb') as f:
    content = f.read()
    ct = content[0x15c100:0x15c100+32]
    file_data = content[0x4660:0x4660+40000-0x20]
print(hexlify(ct))

# dec = unpack('<'+'I'*(0x20//4), ct)
# dec_list = [(dec[i], dec[i+1]) for i in range(0,len(dec),2)]


# def rev(res0, res1):
#     mode = res0
#     v6 = res1
#     for i in range(15,-1,-1):
#         v9 = mode
#         mode = v6
#         v6 = v9 ^ calc(mode, buf[i])
#     res0 = v6
#     res1 = mode
    
#     r0 = hex(res0)[2:]
#     #print(hex(res0))
#     if len(r0) % 2 == 1:
#         r0 = '0'+r0
        
#     r1 = hex(res1)[2:]
#     #print(hex(res1))
#     if len(r1) % 2 == 1:
#         r1 = '0'+r1
#     return unhexlify(r0)[::-1] + unhexlify(r1)[::-1]


# flag_first_part = b'w3lc0mE_t0_Th3_l'
# #rev(0x1df8c5fe, 0xba6b2d80)
# pt = b''
# for i in dec_list:
#     pt += rev(i[0], i[1])
# print("flag:", flag_first_part + pt)


enc = unpack('<'+'I'*((40000-0x20)//4), file_data)
enc_list = [(enc[i], enc[i+1]) for i in range(0,len(enc),2)]
pt = b''
for i in range(len(enc_list)):
    #if i > 100: break
    pt += nom(enc_list[i])

print(len(pt)) #39968

with open('break.new', 'wb') as f:
    new_content = content[:0x4660] + pt + content[0x4660+40000-0x20:]
    f.write(new_content)


# w3lc0mE_t0_Th3_l12345678123456781234567812345678
# w3lc 0mE_ t0_T h3_l
# w3lc0mE_t0_Th3_l4nD_0f_De4th_4nd_d3strUct1oN_4nd_n0_puppi3s@flare-on.com
# obfuscate ((syscall_num^0xdeadbeef)*322423550)&((1<<32)-1)
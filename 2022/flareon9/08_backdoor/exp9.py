with open('test.exe', 'rb') as f:
    code = bytearray(f.read())

from token_data import *
from token_update import update, update_b
from struct import pack

def patch(offset, content):
    code[offset:offset+len(content)] = content

def gen(il, token_map):
    il = bytearray(il)
    if token_map == None:
        return il
    for pos,data in token_map:
        il[pos:pos+4] = pack('<I', data)
    return il

new_code1 = gen(wl_b, wl_m)
new_code2 = gen(gh_b, gh_m)
new_code3 = gen(gs_b, gs_m)
new_code4 = gen(pe_b, pe_m)
new_code5 = gen(d_b, d_m)
new_code6 = gen(cl_b, cl_m)
new_code7 = gen(rt_b, None)

patch(0x1ae10, new_code1) # flared_70 0x55 below
patch(0x19b90, new_code2) # flared_66 0x20c calc hash
# patch(0x1ae9b, b'\x28\xba\x00\x00\x06')
patch(0x1acf8, new_code3) # flared_69 0xac get img_header[hash].data [VirtualSize]
patch(0xabec, new_code4) # flared_35 0x9b get PE info
patch(0xb580, new_code5) # flared_47 0xfa rc4 decrypt above header to code.
patch(0x19e0c, new_code6) # flared_67 0xddc update the token to run the code.
patch(0x1ac5c, new_code7) # flared_68 0x37 many times unpack to uint.


patch(0xaf18, update('flared_38.bin')) # flared_38 0xf8
patch(0xb6dc, update('flared_48.bin')) # flared_48 0xf8

import pefile
pe = pefile.PE("FlareOn.Backdoor.exe")
cand = [
(b"305a002f193b2c1ed9295410535693b9f52c47aaf4f685bccd787b2145af07de", 0x96dc), # 06
(b"4a0fb13652122a0f14c212c36437a5d23d53a19cadf059d11b6bbab3907022e2", 0x9970), # 12
(b"0686a47bcd1172713a20e72108b885853e737a949afdc1cd296f4197944db1e2", 0xb1d4), # 42
(b"2fad6d86f3573b7ceedcb1e688397139901dfc97f1784917d345a22251121627", 0xb520), # 46
(b"7cddb7c1f3d440dea183054eb4576dc8e1d1a4f7ca1fabb5f33fcb1a2a551e29", 0xb8e8), # 50
(b"a4691056b72cb7feda735954953e6ea4b347d8e3735ace8612661d63e1785761", 0xb834), # 49
(b"cc80b00c4bb40917278fde45c00e4e4df426ba455513c251a650878d40bc2d83", 0x9fac), # 19
(b"becb82d3c6bb7eed0697117dec50c26813eb9d9710b85c50842b9b4648d45aef", 0x985c), # 10
(b"3460378b704cb824bf52d41dedc68d99a1afedee8d70267a29841721775572de", 0xa90c), # 31
(b"0651f80b2cb667ae922cbf418343ac73f73956788d9f8a729bab11e1cf35a85e", 0xa660), # 27
(b"edd1976b2b2ba673e1e95247a54238a9b27fb7965bbb117e306524d93e3f99f1", 0xa714), # 29
(b"e712183aad38b4e510347e6968c89b0915acd954e66847b84cd34d687ac021cb", 0x1987c), # 60
(b"710b11bc609c76eddf0b9d50f342e8ba89479aff881fa83407a6262515f7f9f2", 0x199b0), # 63
(b"326aa956a45a5b48c14bd56e606a978d80263a80db167f6e604ff770d65f2f1a", 0x9808), # 09
(b"8d3a199fa17ab158db9c7b072881ce611fae801896acb5b18b8836147222feef", 0x19714), # 58
(b"77c01ab26f569d1a8fb3571757e6a1beed94d3ae2a168fba2fc01c07216c6f8b", 0xb4a4), # 45
(b"719ee568522cdb7a4519108d0a34b9531404122d12775ae8daedafc6f068a016", 0xb3dc), # 44
(b"74fbaf68c82f81c33b3f74468e96439ac6abe8c24f405b2dc0d97cfaebcdc91b", 0xb314), # 43
(b"1b8e223862dbfda65e539a98367650c1f80080f5470117c4cf5d77548d90debc", 0x197dc), # 59
(b"e712183aad38b4e510347e6968c89b0915acd954e66847b84cd34d687ac021cb", 0x198e4), # 61
(b"794ac8464ceed27c1b1afcf98241435748dae7fe6b4952524b631bf81a1e7c0b", 0x9a34), # 13
(b"c61192c7c844195b942eb02b0b64f71f00dad46f11f99b5419bc6d78a72fefb7", 0xb150), # 41
(b"9181748dca8875decbf8e9ded90515da514028154a2396682a4ffc705e43c4c7", 0xa82c), # 30
(b"4951e5478e0781cc7c74837c1b3897c6beaefcf41f1f92686ee50f627f2ca36b", 0x19ad8), # 65
(b"89b957e3cbcc1acc0649a02914815042749ef4bf809987ac3b24a303f31a37f8", 0x91a0), # 00
(b"689d7525fedc82ecb6ae5046342b45e3bccb57e9f9209f658b3f240d1a74069c", 0x92ec), # 01
(b"30752c497d0229b3fecf3e058c2c8d39a9a46a5f27b02da69c0c5a997e97a80e", 0x9378), # 02
(b"7c5ccd915cbf3032739fa1df6b8578099f01baa6b94aebc638f0dc285ffcc915", 0x93e8), # 03
(b"5ca8a51747ebd16b041721bf56a30cd5f39f1829df27e51eadfba77003a38393", 0x9450), # 04
(b"96c576e472cc6ff877cb1db64b2dbd0494f518d3550b213fe753319665721b6b", 0x950c), # 05
(b"b1c8119c5c717d00c46b7a6c43cf3eda111059ac6b4c6cb4a440575dde65e014", 0x908a), # 07
(b"538fcc692564863f834626beee91b70f1f100389e96a91b9b836d7c65acb0dc5", 0x9794), # 08
(b"7135726c5225c7883449ffdd33bb30f26d4e32cfeb3600d9fcdac23baa43833b", 0x98b0), # 11
(b"94957fff987e7e015868fab12fa7d5b0ee1e7545bacb8c8fa4f07ccdc59b8c3d", 0x9a9c), # 14
(b"0e5cf5d9e4e7fd4b8398ef26d20c04a1308cae65181d584d7acf3f48d88c8e50", 0x9b58), # 15
(b"270860100f1937f49306a3325e8523e80b941ec3124e30704e2f154e0f899c83", 0x9be4), # 16
(b"ee6d9a21346018078a87ea4079959b4ed9cf153ae077c93273ea38c718b00b51", 0x9d90), # 17
(b"c4493ff5f1dc3be5ca9fa51900dbfb69dce66febae5e025cecb68051d27eefef", 0x9e8c), # 18
(b"30b905e5d66a3ad24630f11a9f05c361251881c82487d5aec3614474cfebbaf0", 0xa048), # 20
(b"11d539d6204eadbccd1d370ee6bc6225a8c710d5d2e34e923d7a24876b376ed7", 0xa0ec), # 21
(b"8de5507bdedfad2f1bd4b340eb476abab4442cead1b922e8e18521f7d0cd7f7d", 0xa19c), # 22
(b"4f0f2ca37f08cf119f3185e28118947d704968babe1557b56db844a614098cd7", 0xa24c), # 23
(b"85b3a7dd78eb9d17c2832a9c0bf0db35aa018f34dde74bcf4a47d98409e1ec52", 0xa300), # 24
(b"520c23900a8cc6b701184426230786fc29f82f39b50c6a75b5f7418e34d1c39b", 0xa490), # 25
(b"f965be7303dbadaee57d174da473ba7b9297feb886fb008c1f89e0a125c44519", 0xa5c4), # 26
(b"846fcbb2e5f6c174ad51ca99b9f088effefc36c8e67a37df6019289da27fe09b", 0x909e), # 28
(b"e530c0106f2f9e2498ef8cc04c59d7e721caa3dc018c4c8450e4d395e6e92176", 0xa9b8), # 32
(b"f9a758d38e2e4e3641c0fafbac22ffa3314edbaba50e6e5538e3a99a193def7f", 0xaaac), # 33
(b"f8a2493f82ee664325c6407b5cf8465ee02cfea3a24f6a8037add8e4ba5bb648", 0xab4c), # 34
(b"1aa22d6334aa58ad2077d2f1f4199167ef9912756bbc0389770327b587441730", 0xacf0), # 36
(b"892fac736928f224083e373766972ba02aa77c0b44a1f35033c08cd7da79b25f", 0xad58), # 37
(b"977deaeda5fff073045620bfdd21f0eaf0fa910ae9fdc86b8cfa6f7c5721fdfb", 0xb0a0), # 39
(b"977deaeda5fff073045620bfdd21f0eaf0fa910ae9fdc86b8cfa6f7c5721fdfb", 0xb0f8), # 40
(b"db08afea48362227ed638d9657ac36f30eec90853f33fe4c68898b122260f989", 0xb9d0), # 51
(b"81e1a476823fefa6bcb79f32d479c6c07298cd32991be20324e6259e49f7d045", 0xbab0), # 52
(b"ede0bad0a05130663ac46fbc858f0376a5a753edd6a7111831e8951f0f537409", 0xbb34), # 53
(b"699fdcf2eb7d280a3bfaaf7e81a2eb138804737ab5f90ff369ecf8550b59da95", 0xbba0), # 54
(b"33d51cd2fbaef784d7acbc6d5e5cfcce1be1771d3524511a09712c9f541bd36d", 0xbc78), # 55
(b"4ea4cf8de819a44de373cd43d1dd3eedd2d85b497d2dc620e85aa350f264f787", 0xbd28), # 56
(b"310d4de08e81de33d5601d3d7912008f20b2b7749f06566e52db6a77e1f4bdc5", 0xbfe8), # 57
(b"69991a3e95c5119fa78d5cffeff4bd913768663e601fcf7fd028ec252aab1571", 0x1994c), # 62
(b"807617625d41107bf8992c570a8669c792bf094237b2fdbbf2b63a0258fd77e2", 0x19a4c), # 64
]
'''
12 write agent.id to file

42 43 MT19937 generate next random
44 get random value in 58 (shuffle the chars_domain)
59 gen 1st domain name 
10 get counter val
11 get agent id
61 63 str += chars_counter[index % 36]; index/=36; 'p6' left padding to length=3 using chars_counter[0]
14 40 get the domain tail

65 retry

31 接受回调函数，29就是第一位，
30 resolve DNS
29 generate DGA wrapped by 27

26 

从A到C
从C到B 失败
从C到D 成功
F13 F7-B/C
如果23 成功 将 -> D，并且得到FLARE14.ListData F5-E 也会被填满F5-C长度。 F5-D unknown
E cmd 并将结果保存在F5-H（长度F5-F）
24 from F -> B C G F
25 from G -> B D H F

flare56 and flare 54 is the key point!
'''


def long_run(h):
    b = None
    for section in pe.sections:
        if h.startswith(section.Name):
            offset = section.PointerToRawData
            b = code[offset:offset+section.Misc_VirtualSize]
            break

    from Crypto.Cipher import ARC4 as rc4cipher
    def rc4_crypto(c, k):
        enc = rc4cipher.new(k)
        res = enc.decrypt(c)
        return res

    init_key = b'\x12\x78\xab\xdf'
    k = bytes([init_key[i%len(init_key)] for i in range(256)])
    b = rc4_crypto(b, k)
    return bytearray(b)


for _h, _o in cand:
    patch(_o, update_b(long_run(_h)))
        
with open('test.exe', 'wb') as f:
    f.write(code)
tbl = "old new current version process thread id identity task disk keyboard monitor class archive drive message link template logic protocol console magic system software word byte timer window scale info char calc map print list section name lib access code guid build warning save load region column row language date day false true screen net info web server client search storage icon desktop mode project media spell work security explorer cache theme solution "
tbl = tbl.split(' ')[:-1]
l = [0x03, 0x03, 0x07, 0x07, 0x07, 0x06, 0x02, 0x08, 0x04, 0x04, 0x08, 0x07, 0x05, 0x07, 0x05, 0x07, 0x04, 0x08, 0x05, 0x08, 0x07, 0x05, 0x06, 0x08, 0x04, 0x04, 0x05, 0x06, 0x05, 0x04, 0x04, 0x04, 0x03, 0x05, 0x04, 0x07, 0x04, 0x03, 0x06, 0x04, 0x04, 0x05, 0x07, 0x04, 0x04, 0x06, 0x06, 0x03, 0x08, 0x04, 0x03, 0x05, 0x04, 0x06, 0x03, 0x04, 0x03, 0x06, 0x06, 0x06, 0x07, 0x04, 0x07, 0x04, 0x07, 0x05, 0x05, 0x04, 0x08, 0x08, 0x05, 0x05, 0x08]

def randstr(p2, a):
    v7 = 0
    cand = []
    ll = []
    #l = []
    while p2 != 0 and v7 < 8:
        x = ((p2 + v7) & 0xff) + 0x55707B4EFB307BFA
        x ^= (x >> 12)
        x ^= (x << 25) & ((1<<64)-1)
        x ^= (x >> 27)
        v2 = (x * 0x2545F4914F6CDD1D) & ((1<<64)-1)
        index = (v2&0xffff) % len(tbl)
        #print(hex(index))
        v = l[index]
        if ((v2 >> 0x20) & 1) == 0:
            v3 = v
        else:
            v3 = ((v2 >> 0x20) & 0xffff)%(v-1) + 2
        #print(v3)
        ll.append(v3)
        cand.append(tbl[index])
        v7 += 2
        p2 >>= 8
    
    #ll = ll[::-1]
    ans = ''
    for i in range(len(cand)):
        if a & (1<<i):
            cand[i] = chr(ord(cand[i][0]) - 32)+ cand[i][1:]
        ans += cand[i][:ll[i]]
        
    print(ans)

randstr(0xf0f,1)
randstr(0x1010,1)
randstr(0x8576B0D0, 5)
randstr(0x224C6C42, 5)
randstr(0xD6306E08, 5)
print("--------")
randstr(1799, 3)
randstr(0X7F7F, 3)
print("--------")
randstr(5911, 4)
randstr(5911, 3)
randstr(5654, 3)
randstr(2570, 3)
randstr(2570, 4)
randstr(6168, 4)
print("--------")
randstr(7710, 1)
randstr(2313, 11)
randstr(3341, 3)
randstr(3598, 3)
print("--------")
randstr(1285, 1)
randstr(1542, 1)
randstr(4883, 3)
randstr(6682, 4)

randstr(0xd722afcb, 5)

from binascii import unhexlify

def dec(index, es):
    ans = ''
    for i in range(0, len(es), 4):
        t = unhexlify(es[i:i+4])
        ans += chr(t[0] - t[1])
    print(index, ans)
    return ans

def xor(s, offset, bibble, l):
    index = 0
    ans = [0 for i in range(l)]
    for i in range(0, len(s), 4):
        ans[index] = int(s[i+offset:i+2+offset], 16) ^ bibble[index%len(bibble)]
        index += 1
        if index == l:
            return bytes(ans[:l])

xertz = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE]

L = "9655B040B64667238524D15D6201.B95D4E01C55CC562C7557405A532D768C55FA12DD074DC697A06E172992CAF3F8A5C7306B7476B38.C555AC40A7469C234424.853FA85C470699477D3851249A4B9C4E.A855AF40B84695239D24895D2101D05CCA62BE5578055232D568C05F902DDC74D2697406D7724C2CA83FCF5C2606B547A73898246B4BC14E941F9121D464D263B947EB77D36E7F1B8254.853FA85C470699477D3851249A4B9C4E.9A55B240B84692239624.CC55A940B44690238B24CA5D7501CF5C9C62B15561056032C468D15F9C2DE374DD696206B572752C8C3FB25C3806.A8558540924668236724B15D2101AA5CC362C2556A055232AE68B15F7C2DC17489695D06DB729A2C723F8E5C65069747AA389324AE4BB34E921F9421.CB55A240B5469B23.AC559340A94695238D24CD5D75018A5CB062BA557905A932D768D15F982D.D074B6696F06D5729E2CAE3FCF5C7506AD47AC388024C14B7C4E8F1F8F21CB64"
LL = L.split(".")
LLL = []
for i in range(len(LL)):
    LLL.append(dec(i, LL[i]))

print("TEST:", LLL[0])
music = xor(T, 0, xertz, 168667)

print(len(music))
with open("test.mp3", "wb") as f:
    f.write(music)

tok = [ord(i) for i in "FLARE-ON"[::-1]]
pic = xor(T, 2, tok, 285729)
print(len(pic))
with open("v.png", "wb") as f:
    f.write(pic)
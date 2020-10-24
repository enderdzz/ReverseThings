from base64 import b64encode, b64decode
from solve import c

with open("new.dll", "rb") as f:
    content = bytearray(f.read())
    ori = content[0x6390: 0x6390+9]
    print(ori)
    patches = b"\xBB\x9E\x99\x61\xB9\xEB\x1B\x90\x90"
    
print(b64decode(c).find(ori, 28560))
print(b64encode(b64decode(c).replace(ori, patches)))
#print(b64encode(content))
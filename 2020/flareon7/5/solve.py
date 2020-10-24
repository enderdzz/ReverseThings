from hashlib import sha256
passwd = [62,38,63,63,54,39,59,50,39] # >&??6';2'
hash_ans = [50,148,76,233,110,199,228,72,114,227,78,138,93,189,189,147,159,70,66,223,123,137,44,73,101,235,129,16,181,139,104,56] # SHA256
Password = ''.join([chr(i^83) for i in passwd])
hash_ans = ''.join([hex(i)[2:] for i in hash_ans])
print(hash_ans)
# App.Password + App.Note + App.Step + App.Desc

Note = "keep steaks for dinner"
Step = "magic"
Desc = "water"

key = [Desc[2],
Password[6],
Password[4],
Note[4],
Note[0],
Note[17],
Note[18],
Note[16],
Note[11],
Note[13],
Note[12],
Note[15],
Step[4],
Password[6],
Desc[1],
Password[2],
Password[2],
Password[4],
Note[18],
Step[2],
Password[4],
Note[5],
Note[4],
Desc[0],
Desc[3],
Note[15],
Note[8],
Desc[4],
Desc[3],
Note[4],
Step[2],
Note[13],
Note[18],
Note[18],
Note[8],
Note[4],
Password[0],
Password[7],
Note[0],
Password[4],
Note[11],
Password[6],
Password[4],
Desc[4],
Desc[3]]

iv = b"NoSaltOfTheEarth"
key = str.encode(''.join(key))
print("key len:", len(key),key)
m = sha256()
ct = str.encode(Password+Note+Step+Desc)
m.update(ct)
print(m.digest())

new_key = sha256()
new_key.update(key)
key = new_key.digest()

l = 83392 # bytes
# with open("src/bin/TKApp.dll", 'rb') as f:
#     ct = f.read()[0x1a6f: 0x1a6f+l]

with open("Runtime.dll", 'rb') as f:
    ct = f.read()[0:l]

from Crypto.Cipher import AES
enc = AES.new(key, AES.MODE_CBC, IV=iv)
pt = enc.decrypt(ct)

from base64 import b64decode
pic = b64decode(pt)
with open("flag.jpg", 'wb') as f:
    f.write(pic)
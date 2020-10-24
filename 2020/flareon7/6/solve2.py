import win32api
from binascii import unhexlify
from hashlib import sha256
from Crypto.Cipher import AES
from struct import unpack
from ctypes import *

def ROL(data, shift, size=8):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)
     
 
def ROR(data, shift, size=8):
    shift %= size
    body = data >> shift
    remains = (data << (size - shift)) - (body << size)
    return (body + remains)


computer_name = 'aut01tfan1999'

ct = "CD4B32C650CF21BDA184D8913E6F920A37A4F3963736C042C459EA07B79EA443FFD1898BAE49B115F6CB1E2A7C1AB3C4C25612A519035F18FB3B17528B3AECAF3D480E98BF8A635DAF974E0013535D231E4B75B2C38B804C7AE4D266A37B36F2C555BF3A9EA6A58BC8F906CC665EAE2CE60F2CDE38FD30269CC4CE5BB090472FF9BD26F9119B8C484FE69EB934F43FEEDEDCEBA791460819FB21F10F832B2A5D4D772DB12C3BED947F6F706AE4411A52"
def get_computerName():
    host=win32api.GetComputerName()
    print(host)

    with open('sprite.bmp', 'rb') as f:
        content = f.read()[54:]

    lsb = ''
    for i in content:
        lsb += str(i&1)
    
    step = 7 # holly shit, so guessy.
    with open('computer_name', 'w', encoding='utf-8') as f:
        a = ''
        for i in range(0, len(lsb), step):
            a += chr(int(lsb[i:i+step], 2))

        f.write(a)    

class C(Structure):
    _fields_ = [("w", c_int), ("h", c_int), ("c", c_ubyte*3918)]

class O(Structure):
    _fields_ = [("o", c_ubyte*891)]

def solve():
    raw = ""
    for i in computer_name:
        raw += chr(ROR(ord(i)+ord(i), 1))
    h = sha256()
    h.update(str.encode(raw))
    hash32 = h.digest()
    print(hash32)
    
    cipher = AES.new(hash32, AES.MODE_CBC, iv=b'\x00'*16)
    pt = cipher.decrypt(unhexlify(ct))
    pt = pt[:-(11+5)]
    print(pt)
    w,h = unpack('<II', pt[5:13])
    print(w, h)

    qrcode = cdll.LoadLibrary("./qr_code.dll")
    buf = [int(i) for i in pt[13:]+b"\0"*(3918-len(pt[13:]))]
    p = C(w, h, (c_ubyte * len(buf))(*buf) )
    func = qrcode.justConvertQRSymbolToBitmapPixels
    #p = create_string_buffer(pt[5:]+b"\0"*10)
    #print(sizeof(p), repr(p.raw))
    output = create_string_buffer(b"Hello!", 1500)
    buf = [0 for i in range(33*3*9)]
    output = O((c_ubyte * len(buf))(*buf))
    #func.argtypes = [c_char_p, c_char_p]
    func.restype = c_int
    #ret = func(byref(p), byref(output))
    #print("calling done!")

    print(len(pt[13:]))

solve()
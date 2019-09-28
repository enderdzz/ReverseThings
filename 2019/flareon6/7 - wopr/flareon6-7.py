import hashlib, io, lzma, pkgutil, random, struct, sys, time
from ctypes import *
print('LOADING...')
BOUNCE = b"\xaf\xbcbU\xfb\t\xd0Uf\x17JEQ\x12\xcc\x14I\t\xc8\xff\xe9\x92H\x9e\x9cs\x00\xa8\x84S\xb4E\x9d;!\xb9e\x10@\x0c\xca,:X)\x9e\x08\xf3t\x86\xbb\xbf\x8e\x8d\xd8\xe1\xd8\xce\x03x[\xa4\xd3\xaf\xff\x8b,\xc9\x0bHv\xbf\x1a\x8ah\x04]:;\xd9\xd7B\xb0\xac\xb8}`\xde\x0f\x16\xc4\xe1\x01\xb4\xbb\xe5pmx\xc6\x94\x1c\x83\xd9\xfed's\xe2b\x84\x94\x8fC\x83\xeb\xcf\x87\xb2\x01~\x9b\xaf\x00\xac\x98I\xf21\xc8r\x18\x8c@\xe2\xc65\n\xdc6\x96\xfb\xb8ru\x83\xf4\xf3v.\xbb`\x0e]\xcb\xa8w(\x18\x8e/\xaeP\xb5\xe4\xe1J\x066\xa9\xf8Fl\xbe\xd4\x0b6\xb2\xdeo\xb9\xf8)4\xdb\xb0V=\xb6\x81y\x02\xcd\xb3\xe1\xae\xf7\x85\x82\x84\x8c\x95\x9d\xdeC\x8f\x8c\x03\xad\xc8X\x99\xe8\x86\xf4c\xa7'\x1d\x86\xfe\x0f\xfb\x1f\x12&\xcdS\x91\xbd\x11\x88\xb2c\xcb\x8d\xa9g\xee\xffr\xb2\xef\xbc\x96\xaf\xaa\xf7\xbe\x8f\xf0h\x1e\x86\xbdS" 

def ho(h, g={}):
    k = '__builtins__'
    return g.get(k, k)

a = 1702389091
b = 482955849332
g = ho(29516388843672123817340395359, globals())

def eye(face):
    leg = io.BytesIO()
    for arm in face.splitlines():
        arm = arm[len(arm.rstrip(' \t')):]
        leg.write(arm.encode())
    face = leg.getvalue()
    bell = io.BytesIO()
    x, y = (0, 0)
    for chuck in face:
        taxi = {9:0, 32:1}.get(chuck)
        if taxi is None:
            print("oh shit!")
            continue
        x, y = x | taxi << y, y + 1
        if y > 7:
            bell.write(bytes([x]))
            x, y = (0, 0)
    return bell.getvalue() 

def fire(wood, bounce):
    meaning = bytearray(wood)
    bounce = bytearray(bounce)
    regard = len(bounce)
    manage = list(range(256))

    def prospect(*financial):
        return sum(financial) % 256

    def blade(feel, cassette):
        cassette = prospect(cassette, manage[feel])
        manage[feel], manage[cassette] = manage[cassette], manage[feel]
        return cassette

    cassette = 0
    for feel in range(256):
        cassette = prospect(cassette, bounce[(feel % regard)])
        cassette = blade(feel, cassette)

    cassette = 0
    for pigeon, _ in enumerate(meaning):
        feel = prospect(pigeon, 1)
        cassette = blade(feel, cassette)
        meaning[pigeon] ^= manage[prospect(manage[feel], manage[cassette])]

    return bytes(meaning)


with open("poem", 'r') as f:
    doc = f.read()
num = 0
for i in range(74, 75):
    try:
        num += 1
        aa = lzma.decompress(fire(eye(doc), bytes([i]) + BOUNCE))
        print(num)
        with open('final.py', 'wb') as f:
            f.write(aa)
        print(aa)
    except Exception as e:
        continue
        raise(e)
    

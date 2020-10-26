from serpent import *
from struct import unpack
import sys

def s_decrypt():
    serpent_key = b'\xcc;\x07HC\xec\xb3\xdd\xb5>\x19\xc1\x07\xd9j\x92'
    with open('C_DLL/RowmapGuiprotocol_export.dll', 'rb') as f:
        rowman = f.read()
    dat = rowman[0x10400:0x10400+0xe0]
    ans = serpent_cbc_decrypt(serpent_key, dat[:128], iv='\x00'*16)
    with open('final.dat', 'wb') as f:
        f.write(ans)
    
def decrypt(root, path, name):
    # serpent_key = "-N\xCE\fa\xBE)I^\x9D<\xF4\x9A\xB7\xA9@"
    
    # data = "6<\xCD\f\xBC\xD0%\xA3\xD7\x8A^\xA4""8X\xC1n" + "\x05\x18""e\xAE\xEC\x99\fp\x01\xE7\xF2\x14\x94\xAC\x13`"
    # first_key = "\xD4\xB4\xCDv\xC4\xD2V9\x14""AP\xE3|\xD8\xD2:"
    
    # with open("0x110_1.dat", 'rb') as f:
    #     c = f.read()
    # ans = serpent_cbc_decrypt(serpent_key, c, iv='\x00'*16)
    
    # std = "\x8E\xB8k\xDA\x04\x01\x00\x00\x00\x04\x00\x00\xC3\xDA&=\xF1r)3s\xB0""C\x1E\xE0\v\xACL=\xB7#\xBE\xE2\xD9\xCC\xC0\xA7\xEF\x8D\x03h\xC3<W}\xF7\xE6O\tP47\xE9\x17\x85""3\xC9\xF3\xB4\xD4\xEE\xBD\x7F\xE1\a^.U99\xD4<%\xEB\x8A\x89\xA5\xFDz\xD5\xF8\xA5, q:\xE8x\xCF+\x1F""2*\xCF\xE8\xB7\xC5]\xAD`\xB3R\x06\x14\x19\xFAq<\x90=\x9E\xFC""6\xBA\xF9Q\x85\x88\r\x03\xEC\x16ZQ\x18l\xF1\xC3#\xBCX\xC4\v\x85\xFC\xBC\x7F\xA1""b\xAD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00"
    
    # assert std == ans
    
    
    with open(path, 'rb') as f:
        c = f.read()
    name = name[:-3]
    with open(root+"_keys/"+name+'key', 'rb') as f:
        serpent_key = f.read()
    assert len(serpent_key) == 16
    ans = serpent_cbc_decrypt(serpent_key, c, iv='\x00'*16)
    
    _, header_size, code_size, _, _ = unpack("<IIIII", ans[:0x14])
    
    ans = ans[:header_size + code_size]
    #print(repr(ans))
    
    with open(root+"_compressed/"+name+"compressed", 'wb') as f:
        f.write(ans)

# import os
# for root,dirs,files in os.walk(sys.argv[1]):
#     print(files)
#     for _f in files:
#         decrypt(sys.argv[1], sys.argv[1]+'/'+_f, _f)

s_decrypt()
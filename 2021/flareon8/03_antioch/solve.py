from shutil import copyfile
from struct import unpack
from json import loads

import os
import tarfile

name = bytearray(b'Roger the Shrubber\n')

def checksum(name):
    k = 0xffffffff
    for i in range(len(name)):
        k = obfs_tbl[(name[i] ^ k) & 0xff] ^ (k >> 8)
    return 0xffffffff-k

def xor_result(a, b):
    return [a[i]^b[i] for i in range(4096)]

with open("antioch/7016b68f19aed3bb67ac4bf310defd3f7e0f7dd3ce544177c506d795f0b2acf3/AntiochOS", 'rb') as f:
    content = f.read()
    name_tbl = bytearray(content[0x2000:0x2180])
    obfs_tbl = unpack("<"+"I"*256, content[0x2260:0x2260+0x400])

def get_off(name):
    cs = checksum(bytearray(name.encode()+b'\n'))
    for i in range(0, len(name_tbl), 12):

        if cs == unpack("<I", name_tbl[i:i+4])[0]:
            #print(f"Hit {hex(cs)}")
            return name_tbl[i+8]
sorted_dir = ['' for i in range(31)]
for root,dirs,names in os.walk("antioch/"):
    #print(root, names)
    index = [0 for i in range(4096)]
    cur_author = ''
    for filename in names:
        if filename == 'json':
            with open(root + '/' + filename, 'r') as f:
                _ =  loads(f.read())
                if "author" in _:
                    cur_author = _['author']
                    sorted_dir[get_off(_['author'])] = root
                    print(f"{_['author']} OFF #{get_off(_['author'])}")
                    
        # if filename.endswith('.tar'):
        #     print(root, filename)
        #     tar = tarfile.open(root + '/' + filename)
        #     tar.extractall(path=root)
        #     tar.close()
        
        if filename.endswith('.dat'):
            with open(root + '/' + filename, 'rb') as f:
                content = bytearray(f.read())
                #print(root + '/' + filename, len(content))
                #print(index[:20], content[:20])
                index = xor_result(index, content)
    print(root, cur_author)
    ele = "V',`)(//\\\\\\||||||||||||_______________"
    #print(len(ele))
    ele_tbl = ele + '.' * (0x200 - len(ele))
    
    for i in range(0, 4096, 16):
       print(''.join(ele_tbl[j] for j in index[i:i+15]))
print(sorted_dir)

for data_dir in sorted_dir: 
    for root,dirs,names in os.walk(data_dir):
        for filename in names:
            if filename.endswith('.dat'):
                    print(root, filename)
                    copyfile(root+'/'+filename, 'antioch/latest/'+filename)

### 
# after resort the .dat dirs of all layers according to the order retrieved from `approach` function, we cover the original data files with newer ones. And finally recover the right XOR result. It's a wonderful ASCII picture.

# Five-Is-Right-Out@flare-on.com
# -*- coding: utf-8 -*-
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1' #irc server
PORT = 6667 #port
NICK = 'dung3onm4st3r13'
USERNAME = 'dummy'
REALNAME = 'little pony'

print('soc created |', s)
remote_ip = socket.gethostbyname(HOST)
print('ip of irc server is:', remote_ip)


s.connect((HOST, PORT))

print('connected to: ', HOST, PORT)

nick_cr = (f'NICK {NICK}\n').encode()
s.send(nick_cr)
usernam_cr= (f'USER {USERNAME} * * :rainbow pie \n').encode()

import sys
user = sys.argv[1]
data1 = f'PRIVMSG #dungeon :{user}, you enter the dungeon The Sunken Crypt. It is flimsy, gruesome great, dark oppressive, bad, average, virtual, last, more strange, inhospitable, slimy, average, few dismal, flimsy, dark and gruesome, inhospitable, inhospitable, frightening, last, slimy, nicest, solid, dark oppressive, few dismal, deep subterranean, last, gruesome great, average, gruesome great, average, cruel, damned, common, and bad..'

data2 = f'PRIVMSG #dungeon :{user}, you encounter a Wyvern in the distance. It stares at you imposingly. The beast sits in the water, waiting for you to approach it. What do you do?'

filename = 'cool_wizard_meme.png'

full_pattern = b"(.*) on the (.*) for (\d+)d(\d+) damage"
raw_pattern  = b"(.*) on the (.*) for (\d+) raw damage"
only_pattern = b"(.*) on the (.*)"
cast_pattern = b"I cast (.*)!"

with open('output2', 'rb') as f:
    output2 = f.read()
    
def extract_output(data):
    
    phase = bytearray()
    for rawdata in re.findall(cast_pattern, data):
        
        res1 = re.find(full_pattern, rawdata)
        res2 = re.find(raw_pattern, rawdata)
        res3 = re.find(only_pattern, rawdata)
        if res1 != None:
            phase += bytes([tbl_spell.index(res[0]), int(res[2]), int(res[3])])
        elif res2 != None:
            phase += bytes([tbl_spell.index(res[0]), int(res[2])])
        elif res3 != None:
            phase += bytes([tbl_spell.index(res[0])])
    return phase

pt = bytearray()
data = s.recv(4096).decode('utf-8')
if data.find('PING') != -1:
    s.send(str('PONG ' + data.split(':')[1] + '\n').encode())
    print('PONG sent \n')

    time.sleep(1)
    s.send(usernam_cr)
    s.send('JOIN #dungeon \n'.encode()) #chanel
while 1:
    print(data)
    
    find_bytes = False
    
    for cand in range(256):
        pt += bytes([cand])
        with open(filename, 'wb') as f:
            f.write(pt)
        
        s.send(data1)
        
        s.send(data2)
        
        time.sleep(0.5)
        
        data = s.recv(4096).decode('utf-8')
        
        if data.find('PING') != -1:
            s.send(str('PONG ' + data.split(':')[1] + '\n').encode())
            print('PONG sent \n')
            
        cur = extract_output(data)
        
        if cur[-1] == output2[index]:
            
            index += 1
            find_bytes = True
            break
        else:
            pt = pt[:-1]
        
s.close()
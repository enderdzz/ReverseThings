'''
  byte_4060[2 * a1] = v10[1] ^ byte_2020[2 * a1];
  byte_4060[2 * a1 + 1] = v10[1] ^ byte_2020[2 * a1 + 1];
'''
byte_2020 = [0x79, 0x5A, 0xB8, 0xBC, 0xEC, 0xD3, 0xDF, 0xDD, 0x99, 0xA5, 0xB6, 0xAC, 0x15, 0x36, 0x85, 0x8D, 0x09, 0x08, 0x77, 0x52, 0x4D, 0x71, 0x54, 0x7D, 0xA7, 0xA7, 0x08, 0x16, 0xFD, 0xD7]

a=["rook-c3-c6.game-of-thrones.flare-on.com A 127.150.96.223",
"knight-g1-f3.game-of-thrones.flare-on.com A 127.252.212.90",
"pawn-c2-c4.game-of-thrones.flare-on.com A 127.215.177.38",
"knight-c7-d5.game-of-thrones.flare-on.com A 127.118.118.207",
"bishop-f1-e2.game-of-thrones.flare-on.com A 127.89.38.84",
"rook-a1-g1.game-of-thrones.flare-on.com A 127.109.155.97",
"bishop-c1-f4.game-of-thrones.flare-on.com A 127.217.37.102",
"bishop-c6-a8.game-of-thrones.flare-on.com A 127.49.59.14",
"pawn-e2-e4.game-of-thrones.flare-on.com A 127.182.147.24",
"king-g1-h1.game-of-thrones.flare-on.com A 127.0.143.11",
"knight-g1-h3.game-of-thrones.flare-on.com A 127.227.42.139",
"king-e5-f5.game-of-thrones.flare-on.com A 127.101.64.243",
"queen-d1-f3.game-of-thrones.flare-on.com A 127.201.85.103",
"pawn-e5-e6.game-of-thrones.flare-on.com A 127.200.76.108",
"king-c4-b3.game-of-thrones.flare-on.com A 127.50.67.23",
"king-c1-b1.game-of-thrones.flare-on.com A 127.157.96.119",
"queen-d1-h5.game-of-thrones.flare-on.com A 127.99.253.122",
"bishop-f3-c6.game-of-thrones.flare-on.com A 127.25.74.92",
"knight-d2-c4.game-of-thrones.flare-on.com A 127.168.171.31",
"pawn-c6-c7.game-of-thrones.flare-on.com A 127.148.37.223",
"bishop-f4-g3.game-of-thrones.flare-on.com A 127.108.24.10",
"rook-d3-e3.game-of-thrones.flare-on.com A 127.37.251.13",
"pawn-e4-e5.game-of-thrones.flare-on.com A 127.34.217.88",
"queen-a8-g2.game-of-thrones.flare-on.com A 127.57.238.51",
"queen-a3-b4.game-of-thrones.flare-on.com A 127.196.103.147",
"queen-h5-f7.game-of-thrones.flare-on.com A 127.141.14.174",
"pawn-h4-h5.game-of-thrones.flare-on.com A 127.238.7.163",
"bishop-e2-f3.game-of-thrones.flare-on.com A 127.230.231.104",
"pawn-g2-g3.game-of-thrones.flare-on.com A 127.55.220.79",
"knight-h8-g6.game-of-thrones.flare-on.com A 127.184.171.45",
"bishop-b3-f7.game-of-thrones.flare-on.com A 127.196.146.199",
"queen-d1-d6.game-of-thrones.flare-on.com A 127.191.78.251",
"knight-b1-c3.game-of-thrones.flare-on.com A 127.159.162.42",
"bishop-f1-d3.game-of-thrones.flare-on.com A 127.184.48.79",
"rook-b4-h4.game-of-thrones.flare-on.com A 127.127.29.123",
"bishop-c1-a3.game-of-thrones.flare-on.com A 127.191.34.35",
"bishop-e8-b5.game-of-thrones.flare-on.com A 127.5.22.189",
"rook-f2-f3.game-of-thrones.flare-on.com A 127.233.141.55",
"pawn-a2-a4.game-of-thrones.flare-on.com A 127.55.250.81",
"pawn-d2-d4.game-of-thrones.flare-on.com A 127.53.176.56"]

b = ['' for i in range(15)]
for i in range(len(a)):
    ip = a[i].split(' ')[-1].split('.')
    if int(ip[3])&1:
        continue
    b[int(ip[2])&0xf] = ip
for i in b:
    print i
flag = [0 for i in range(30)]
for i in range(15):
    flag[2*i] = int(b[i][1])^byte_2020[2*i]
    flag[2*i+1] = int(b[i][1])^byte_2020[2*i+1]

print ''.join([chr(i) for i in flag])

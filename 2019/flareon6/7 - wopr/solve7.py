from z3 import *
import binascii

h = [26, 134, 152, 207, 160, 167, 187, 17, 79, 79, 207, 201, 3, 194, 248, 151]
h = [15, 136, 228, 11, 45, 245, 7, 190, 116, 220, 215, 203, 123, 9, 125, 41]
h = [167, 117, 182, 196, 113, 122, 88, 6, 111, 51, 209, 31, 19, 173, 233, 228]
h = [115, 29, 32, 68, 106, 108, 89, 76, 21, 71, 78, 51, 75, 1, 55, 102]
#h = [212, 162, 242, 218, 101, 109, 50, 31, 125, 112, 249, 83, 55, 187, 131, 206]
#h = [101, 22, 176, 43, 39, 155, 144, 121, 68, 199, 6, 248, 34, 139, 46, 164]
x = [BitVec('x%d' % i,8) for i in range(16)]
#h = [IntVal(i) for i in h]

solver = Solver()
#for i in range(16):
#    solver.add(x[i]>=32)
#for i in range(16):
#    solver.add(x[i]<=126)
solver.add(h[0] == x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[11] ^ x[14])
solver.add(h[1] == x[0] ^ x[1] ^ x[8] ^ x[11] ^ x[13] ^ x[14])
solver.add(h[2] == x[0] ^ x[1] ^ x[2] ^ x[4] ^ x[5] ^ x[8] ^ x[9] ^ x[10] ^ x[13] ^ x[14] ^ x[15])
solver.add(h[3] == x[5] ^ x[6] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[15])
solver.add(h[4] == x[1] ^ x[6] ^ x[7] ^ x[8] ^ x[12] ^ x[13] ^ x[14] ^ x[15])
solver.add(h[5] == x[0] ^ x[4] ^ x[7] ^ x[8] ^ x[9] ^ x[10] ^ x[12] ^ x[13] ^ x[14] ^ x[15])
solver.add(h[6] == x[1] ^ x[3] ^ x[7] ^ x[9] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[15])
solver.add(h[7] == x[0] ^ x[1] ^ x[2] ^ x[3] ^ x[4] ^ x[8] ^ x[10] ^ x[11] ^ x[14])
solver.add(h[8] == x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[12])
solver.add(h[9] == x[6] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[15])
solver.add(h[10] == x[0] ^ x[3] ^ x[4] ^ x[7] ^ x[8] ^ x[10] ^ x[11] ^ x[12] ^ x[13] ^ x[14] ^ x[15])
solver.add(h[11] == x[0] ^ x[2] ^ x[4] ^ x[6] ^ x[13])
solver.add(h[12] == x[0] ^ x[3] ^ x[6] ^ x[7] ^ x[10] ^ x[12] ^ x[15])
solver.add(h[13] == x[2] ^ x[3] ^ x[4] ^ x[5] ^ x[6] ^ x[7] ^ x[11] ^ x[12] ^ x[13] ^ x[14])
solver.add(h[14] == x[1] ^ x[2] ^ x[3] ^ x[5] ^ x[7] ^ x[11] ^ x[13] ^ x[14] ^ x[15])
solver.add(h[15] == x[1] ^ x[3] ^ x[5] ^ x[9] ^ x[10] ^ x[11] ^ x[13] ^ x[15])

if solver.check() == sat:
    m = solver.model()
    print(m)
    s = []
    for i in range(16):
        s.append(m[x[i]].as_long())
    print(bytes(s))
else:
    print('unsat')
    exit(0)

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

eye = [219, 232, 81, 150, 126, 54, 116, 129, 3, 61, 204, 119, 252, 122, 3, 209, 196, 15, 148, 173, 206, 246, 242, 200, 201, 167, 2, 102, 59, 122, 81, 6, 24, 23]
flag = fire(eye, bytes(s)).decode()
print(flag)

p = [0x1C, 0x5C, 0x22, 0x00, 0x00, 0x17, 0x02, 0x62, 0x07, 0x00, 0x06, 0x0D, 0x08, 0x75, 0x45, 0x17, 0x17, 0x3C, 0x3D, 0x1C, 0x31, 0x32, 0x02, 0x2F, 0x12, 0x72, 0x39, 0x0D, 0x23, 0x1E, 0x28, 0x29, 0x69, 0x31, 0x00, 0x39,0x00]
p = [0x44, 0x29, 0x36, 0x0A, 0x29, 0x0F, 0x05, 0x1B, 0x65, 0x26, 0x10, 0x04, 0x2B, 0x68, 0x30, 0x2F, 0x00, 0x33, 0x2F, 0x05, 0x1A, 0x1F, 0x0F, 0x38, 0x02, 0x18, 0x42, 0x02, 0x33, 0x1A, 0x28, 0x04, 0x2A, 0x47, 0x3F, 0x04, 0x26, 0x64, 0x66, 0x4D, 0x10, 0x37, 0x3E, 0x28, 0x3E, 0x77, 0x1C, 0x3F, 0x7E, 0x36, 0x34,0x2a,0x00]

def solve(v):
  s = []
  for i in range(52):
    s.append(chr(p[i]^ord(v[i%13])))
  s = ''.join(s)  
  if ".com" in s:
    print s#,v

'''
v3_4 = []
for i in xrange(32,127):
  for j in xrange(32,127):
    if i ^ j == 65:
      v3_4.append((i,j))	
v5 = []
for k in xrange(32,127):
  if k&1 == 0:
    v5.append(k)
v = list("RoTq0BeRinG")	
for i in v3_4:
  for j in v5:
    v[3] = chr(i[0])
    v[4] = chr(i[1])
    v[5] = chr(j)
    solve(''.join(v))
'''

solve('\rv[_Z[ZsQPU[G')

from pprint import pprint
with open('vmcode', 'rb') as f:
	M = f.read()
di = {
 '17b0': (0, 'memset 0x400 bytes at +800.'),
 '1950': (2, 'vpaddw'),
 '1a70': (2, 'vpaddd'),
 '1b90': (2, 'vpaddq'),
 '1cb0': (2, 'vpaddb'),
 '1dd0': (2, 'vpand'),
 '1ef0': (2, 'vpcmpeqb'),
 '2010': (1, 'memcpy 32bytes from +0 to'),
 '20d0': (2, 'vpslld'),
 '21e0': (2, 'vpmaddwd'),
 '2300': (2, 'vpmaddubsw'),
 '24e0': (2, 'vpmuldq'),
 '2740': (2, 'vpor'),
 '2860': (2, 'vpermd'),
 '2980': (2, 'vpsrld'),
 '2a90': (2, 'vpshufb'),
 '2bb0': (2, 'vpsubw'),
 '2cd0': (2, 'vpsubd'),
 '2df0': (2, 'vpsubq'),
 '2f10': (2, 'vpsubb'),
 '3030': (2, 'vpxor')}
with open("input2_trace4.txt", 'r') as f:
	a = f.read().strip('\r').split('\n')

pprint(di)
for i in a:
	t = i.strip('\r').split(' ')
	if di[t[0].lower()][0] == 0:
		print "%s" % (di[t[0].lower()][1])
	elif di[t[0].lower()][0] == 1:
		print "%s M[%s]" % (di[t[0].lower()][1], t[4])
		print repr(M[int(t[2],16)+2: int(t[2],16)+34])
	else:
		print "M[%s] = M[%s] %s M[%s]" % (t[4], t[6], di[t[0].lower()][1], t[8])

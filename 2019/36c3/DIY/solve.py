from z3 import *
v1 = "9d5088c4c2122faeb533e75c2c0023ee8bd47e86ffcdbba808c2c8a8627b1b8f"
v2 = "P003I013WI015O1O1RTO2TO2QBO2DE1E1I013O1P000BO1TO1P002LBO1TDE1E1E1I008P003LI004P005LO1P000BO1TO1P002LBO1TDE1E1E1I005O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1I010TI013O1O1NTP000BO2O2TQDO2TO2NDE1E1I002I005O1O1TNO2TO2NDO2O2NP002LDE1E1O1P000BO1TO1P002LBO1TDE1E1E1I009O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1I005P019I012VI003VO1O1TNO2TO2NDO2O2NP002LDE1E1I000O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P004I004VI014I004O1O1TNO2TO2NDO2O2NP002LDE1E1O1P000BO1TO1P002LBO1TDE1E1E1I012O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P003I001WI004I003O1O1RTO2TBO2DE1E1O1P000BO1TO1P002LBO1TDE1E1E1I014O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P014I005I007O1O1RTO2TBO2DE1E1O1O1RTO2TBO2DE1E1I013O1O1RTO2TBO2DE1E1I011O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P001I006O1O1NTP000BO2O2TQDO2TO2NDE1E1I001O1O1TNO2TO2NDO2O2NP002LDE1E1P001I007O1O1NTP000BO2O2TQDO2TO2NDE1E1I002WO1O1RTO2TO2QBO2DE1E1I007O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P011P001I013I014O1O1RTO2TBO2DE1E1HO1O1RTO2TBO2DE1E1I015O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1I012I006O1P000BO1TO1P002LBO1TDE1E1E1I012O1O1RTO2TBO2DE1E1I006O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P002I001WP002I014WO1O1RTO2TBO2DE1E1P001HI001O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1I004I001I003O1P000BO1TO1P002LBO1TDE1E1E1O1O1TNO2TO2NDO2O2NP002LDE1E1I008O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P001P001I009I000O1O1RTO2TBO2DE1E1WHI003O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P003I010I009O1P000BO1TO1P002LBO1TDE1E1E1HI004O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1P007I006O1O1NTP000BO2O2TQDO2TO2NDE1E1P001I010TO1O1RTO2TBO2DE1E1HI010O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1I012I004O1O1RTO2TBO2DE1E1I002O1P000BO1TO1P002LBO1TDE1E1E1O1O1RTO2TO2QBO2DE1E1"

passwd = '0123456789123456'
passwd = [BitVec('pass_%d' % i, 8) for i in range(16)]
s = Solver()

for c in passwd:
	s.add(c >= 0x20)
	s.add(c < 0x7f)

v4 = len(v2)
v6 = 0
v3 = []
while v6 < v4:
    v5 = v2[v6]
    if v5 == 'P': # -- imm
        v6 += 1
        v7 = v2[v6:v6+3]
        v6 += 3
        v3.append(int(v7))
    elif v5 == 'I': # -- chr
        v6 += 1
        v8 = v2[v6:v6+3]
        v6 += 3
        # v8 = ord(passwd[int(v8)]) ## TODO: NOTE: Careful ord()!
        v8 = passwd[int(v8)]
        v3.append(v8)
    elif v5 == 'D': # -- a+b
        v6 += 1
        # v11 = len(v3)
        # v11 -= 1
        # v12 = v3[v11]
        # del v3[v11]
        # v11 -= 1
        # v13 = v3[v11]
        # del v3[v11]
        v12 = v3.pop()
        v13 = v3.pop()

        # v14 = ''
        # v15 = 0
        # v16 = v12
        # while v15 < 8:
        #     v17 = v16 & 1
        #     v14.append(v17)
        #     v16 = v16 >> 1
        #     v15 += 1
        # v17 = 0
        # v16 = 0
        # while v16 < 8:
        #     v15 = v14[v16]
        #     if !v15:
        #         v17 = v17 +(1<<v16)
        #     v16 += 1
        v17 = v12 ^ 0xff

        v18 = v12 ^ v13
        v19 = v17 | v13
        v19 = v19 + v19
        v20 = v17 * 2
        v21 = 255 & (v18+v19-v20)
        v3.append(v21)

    elif v5 == 'B': # -- a-b
        v6 += 1
        # v22 = len(v3)
        # v22 -= 1
        # v23 = v3[v22]
        # del v3[v22]
        # v22 -= 1
        # v24 = v3[v22]
        # del v3[v22]
        v23 = v3.pop()
        v24 = v3.pop()

        v24 = (-v24) & 0xff ## TODO: NOTE: Careful & 0xff!
        # v25 = ''
        # v26 = 0
        # v27 = v24
        # while v26 < 8:
        #     v28 = v27 & 1
        #     v25.append(v28)
        #     v27 = v27 >> 1
        #     v26 += 1
        # v28 = 0
        # v27 = 0
        # while v27 < 8:
        #     v26 = v25[v27]
        #     if !v26:
        #         v28 += (1<<v27)
        #     v27+=1
        v28 = v24 ^ 0xff
        v29 = v23 & v28
        v30 = v23 & v24
        v31 = 255 & (v24+v29+v30)
        v3.append(v31)
    elif v5 == 'L': # -- a*b
        v6 += 1
        # v32= len(v3)
        # v32 -= 1
        # v33 = v3[v32]
        # del v3[v32]
        # v32 -= 1
        # v34 = v3[v32]
        # del v3[v32]
        v33 = v3.pop()
        v34 = v3.pop()

        v35 = v34 ^ (0xff) ## TODO: NOTE: Careful -1!
        v36 = -2
        v37 = 0
        while v33 > 0:
            v38 = v37 ^(0xff) ## TODO: NOTE: Careful -1!
            v37 = 255 & (-v38-v35+v36)
            v33 -= 1
        v3.append(v37)
    elif v5 == 'V': # -- a/b
        v6 += 1
        # v39 = len(v3)
        # v39 -= 1
        # v40 = v3[v39]
        # del v3[v39]
        # v39 -= 1
        # v41 = v3[v39]
        # del v3[v39]
        v40 = v3.pop()
        v41 = v3.pop()

        '''
        v42 = 0 
        v43 = -v41
        v44 = v43 ^ (0xff) ## TODO: NOTE: Careful -1!
        while v40 >= v41:
            v45 = v43 ^ v40
            v46 = 2*(v44|v40)
            v47 = 2*v44
            v40 = v45+v46-v47
            v42 += 1
        '''
        v3.append(v40 / v41)
    elif v5 == 'R': # -- a^b
        v6 += 1
        # v48 = len(v3)
        # v48 -= 1
        # v60 = v3[v48]
        # del v3[v48]
        # v48 -= 1
        # v61 = v3[v48]
        # del v3[v48]
        v60 = v3.pop()
        v61 = v3.pop()

        v49 = (v60 + v61) & 0xff ## TODO: NOTE: Careful & 0xff!
        v50 = v60 & v61
        v51 = v60 & v61
        v52 = 255 & (v49-v50-v51)
        v3.append(v52)
    elif v5 == 'Q': # -- a|b
        v6 += 1
        # v53 = len(v3)
        # v53 -= 1
        # v54 = v3[v53]
        # del v3[v53]
        # v53 -= 1
        # v55 = v3[v53]
        # del v3[v53]
        v54 = v3.pop()
        v55 = v3.pop()

        # v56 =''
        # v57 = 0
        # v58 = v54
        # while v57 <8:
        #     v59 = v58&1
        #     v56.append(v59)
        #     v58 = v58 >> 1
        #     v57 += 1
        # v59 = 0
        # v58 = 0
        # while v58 <8:
        #     v57 = v56[v58]
        #     if !v57:
        #         v59 = v59+(1<<v58)
        #     v58 += 1
        v59 = v54 ^ 0xff
        v62 = v54 ^ v55
        v63 = v59 | v55
        v64 = 255 & (v63+v62-v59)
        v3.append(v64)
    elif v5 == 'N': # -- a&b
        v6 += 1
        # v65 = len(v3)
        # v65 -= 1
        # v66 = v3[v65]
        # del v3[v65]
        # v65 -= 1
        # v67 = v3[v65]
        # del v3[v65]
        v66 = v3.pop()
        v67 = v3.pop()

        # v68 = ''
        # v69 = 0
        # v70 = v67
        # while v69 <8:
        #     v71 = v70&1
        #     v68.append(v71)
        #     v70 = v70 >> 1
        #     v69 += 1
        # v71 = 0
        # v70 = 0
        # while v70 <8:
        #     v69 = v68[v70]
        #     if !v69:
        #         v71 = v71+(1<<v70)
        #     v70 += 1
        v71 = v67 ^ 0xff

        v72 = (-(v66^v67)) & 0xff ## TODO: NOTE: Careful & 0xff!
        v73 = v66 & v71
        v74 = (v72+v73+v67)
        v3.append(v74)
    elif v5 == 'H': # -- a<<b 
        v6 += 1
        # v75 = len(v3)
        # v75 -= 1
        # v76 = v3[v75]
        # del v3[v75]
        # v75 -= 1
        # v77 = v3[v75]
        # del v3[v75]
        v76 = v3.pop()
        v77 = v3.pop()

        v76 = 255 & (v76<<v77)
        v3.append(v76)
    elif v5 == 'W': # -- a>>b
        v6 += 1
        # v78 = len(v3)
        # v78 -= 1
        # v79 = v3[v78]
        # del v3[v78]
        # v78 -= 1
        # v80 = v3[v78]
        # del v3[v78]
        v79 = v3.pop()
        v80 = v3.pop()

        v79 = v79 >> v80
        v3.append(v79)
    elif v5 == 'T': # -- ~a
        v6 += 1
        # v81 = len(v3)
        # v81 -= 1
        # v82 = v3[v81]
        # del v3[v81]
        v82 = v3.pop()
        # v83 = ''
        # v84 = 0
        # while v84<8:
        #     v85 = v82 &1
        #     v83.append(v85)
        #     v82 = v82 >> 1
        #     v84 += 1
        # v86 =0
        # v82 =0
        # while v82 <8:
        #     v84 = v83[v82]
        #     if !v84:
        #         v86 = v86 + (1<<v82)
        #     v82 += 1
        v86 = v82 ^ 0xff
        v3.append(v86)
    elif v5 == 'O': # -- pick
        v6 += 1
        v87 = int(v2[v6])
        v6 += 1
        v88 = len(v3)
        v88 = v88 - 1 - v87
        v89 = v3[v88]
        v3.append(v89)
    elif v5 == 'E': # -- nip
        v6 += 1
        v90 = int(v2[v6])
        v6 += 1
        v91 = len(v3)
        v91 = v91 - 1 - v90
        del v3[v91]

s.add(v3[0] == 0)

if s.check() == sat:
	m = s.model()
	print("".join([ chr(int("%r" % m.evaluate(c))) for c in passwd ]))
#if v3[0] == 0 && len(v3) == 1:
#    print("success")

'''
#v93 = v1[0]
v95 = '0'
s_len = len(v93)
v1 = ''

while v95 < s_len:
    b = v93[v95]
    v95 += 1
    v96 = v93[v95]
    v95 += 1
    if b == 'a':
        b = 10
    elif b == 'b':
        b = 11
    elif b == 'c':
        b = 12
    elif b == 'd':
        b = 13
    elif b == 'e':
        b = 14
    elif b == 'f':
        b = 15
    v96 = int('0x'+v96, 16)
    v97 = b*16 +v96
    v1.append(v97)
'''
# import binascii
# v93 = "9d5088c4c2122faeb533e75c2c0023ee8bd47e86ffcdbba808c2c8a8627b1b8f"
# v98 = binascii.unhexlify(v93)
# key = ''
# v99 = 0
# while v99 < 32:

#     v100 = v98[v99]
#     v101 = v99 % 16
#     v102 = passwd[v101]
    
#     v102 = ord(passwd[v101])
#     v105 = v102 ^ v100
#     v106 = "0123456789abcdef"
#     v97 = v105%16
#     v107 = v106[v97]
#     v97 = v105/16
#     v108 = v106[v97]
#     v109 = v108 + v107
#     key.append(v109)
#     v99 += 1
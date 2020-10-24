from struct import pack

val2 = [0x2C332323,0x49643F0E,0x40A1E0A,0x1A021623,0x24086644,745804082,255995178,224677950,387646557,84096534,134815796,237248867,1479808021,981018906,1482031104,0x54]

val = [0x3B020E38, 0x341B3B19, 0x3E230C1B, 0x42110833, 0x731E1239]

ct = b''.join([pack('<i', i) for i in val2])

buf1 = "nPTnaGLkIqdcQwvieFQKGcTGOTbfMjDNmvibfBDdFBhoPaBbtfQuuGWYomtqTFqvBSKdUMmciqKSGZaosWCSoZlcIlyQpOwkcAgw "
buf2 = "KglPFOsQDxBPXmclOpmsdLDEPMRWbMDzwhDGOyqAkVMRvnBeIkpZIhFznwVylfjrkqprBPAdPuaiVoVugQAlyOQQtxBNsTdPZgDH "

print(''.join([chr(ct[i]^ord(buf1[i%102])) for i in range(61)]))
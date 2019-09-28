with open("PYC124.pyc", 'rb') as f:
    with open("poem", 'wb') as g:
        g.write(f.read()[0x16e:0x8f94])
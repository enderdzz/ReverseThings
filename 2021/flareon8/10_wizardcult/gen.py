a = b''.join([bytes([i])*24 for i in range(256)])
with open('root/cool_wizard_meme.png', 'wb') as f:
    f.write(a)
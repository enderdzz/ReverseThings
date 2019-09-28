import pefile

with open('876.dmp', 'rb') as f:
    content = f.read()
    
c = content[0x29301c: 0x29601C]
n = content[0x29601C: 0x2A001C]
k = content[0x2A001C: 0x2A701C]
s = content[0x2A701C: 0x2AC01C]
ff = content[0x2AC01C: 0x3E100C]
stm = content[0x24700C: 0x29301C]
driver1 = content[0x3e100c: 0x54B8A5]
last1 = content[0x1ACF5100: 0x1AD49F4B]
last2 = content[0x1AF27040: 0x1AF3CE08]

with open('c.dll', 'wb') as t:
    t.write(c)
with open('n.dll', 'wb') as t:
    t.write(n)
with open('k.dll', 'wb') as t:
    t.write(k)
with open('s.dll', 'wb') as t:
    t.write(s)
with open('f.dll', 'wb') as t:
    t.write(ff)
with open('stm.dll', 'wb') as t:
    t.write(stm)
with open('driver1.dll', 'wb') as t:
    t.write(driver1)
with open('last1.dll', 'wb') as t:
    t.write(last1)
with open('last2.dll', 'wb') as t:
    t.write(last2)


#pe = pefile.PE(data=res)
#print hex(pe.OPTIONAL_HEADER.SizeOfImage)


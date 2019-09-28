import string
import base64
#from Crypto.Cipher import DES
#import sys
s = ""
custom = "ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"
Base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
ciphertext = 'x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q'
for ch in ciphertext:
	if (ch in Base64):
		s = s + Base64[string.find(custom,str(ch))]
	elif (ch == '='):
		s += '='
#s += '=='
print s
result = base64.decodestring(s)
print result

# c2gwMHRpbmdfcGhpc2hfaW5fYV9iYXJyZWxAZmxhcmUtb24uY29t
# sh00ting_phish_in_a_barrel@flare-on.com


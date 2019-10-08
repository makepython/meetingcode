s1 = 'hello'
s2 = '猫'

import binascii

print(binascii.hexlify('\u1023'.encode('utf-16')))
print(binascii.hexlify('\U00011023'.encode('utf-16')))
print(binascii.hexlify('\u1023'.encode('utf-8')))
print(binascii.hexlify('\U00011023'.encode('utf-8')))

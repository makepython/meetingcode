import sys
import struct
print("{0:.50g}".format(0.1))
print("{0:.50g}".format(0.2))
print("{0:.50g}".format(0.3))
print("{0:.50g}".format(0.1+0.2))

print(" ".join(reversed(list(map(lambda x: bin(x)[2:].zfill(8), struct.pack('@f', 0.5))))))
# 00111111 00000000 00000000 00000000
# sign exp-127  mantissa
# 0    01111110 00000000000000000000000
# 0b01111110-127 = 126-127 = -1
# Implicit one for mantissa
# 1 * 2**-1
# 0.5


print(" ".join(reversed(list(map(lambda x: bin(x)[2:].zfill(8), struct.pack('@f', 0.26171875))))))
# 00111110 10000110 00000000 00000000
# 0 01111101 00001100000000000000000
# 0 125-127=-2  1.00001100000000000000000
# (1 + 1 * 2^-5 + 1 * 2^-6) * 2^-2 = 0.26171875

# BE LE
struct.pack('<I',0xaabbccdd)
# '\xdd\xcc\xbb\xaa'
struct.pack('>I',0xaabbccdd)
# '\xaa\xbb\xcc\xdd'

print(sys.byteorder)

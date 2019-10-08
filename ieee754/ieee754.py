import struct
print("{0:.50g}".format(0.1))
print("{0:.50g}".format(0.2))
print("{0:.50g}".format(0.3))
print("{0:.50g}".format(0.1+0.2))

print(list(map(bin, struct.pack('@f', 1))))
# ['0b0', '0b0', '0b10000000', '0b111111']
# 0b01111110-127
# -1
# 2**-1
# 0.5

# BE LE
struct.pack('<I',0xaabbccdd)
# '\xdd\xcc\xbb\xaa'
struct.pack('>I',0xaabbccdd)
# '\xaa\xbb\xcc\xdd'

print(sys.byteorder)

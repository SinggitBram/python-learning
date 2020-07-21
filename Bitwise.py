a = 972
b = 5
print(a, format(a, '08b'))
print(b, format(b, '08b'))

# bitwise or
c = a | b
print(c, format(c, '08b'))

# bitwise and
c = a & b
print(c, format(c, '08b'))

# bitwise xor
c = a ^ b
print(c, format(c, '08b'))

# bitwise not
c = ~a
print(c, format(c, '08b'))

d = 0b00000001
e = 0b11111111
print(e ^ d)

# shifting
c = a >> 1
d = a >> 2
e = a<<5
print(c)
print(d)
print(e)

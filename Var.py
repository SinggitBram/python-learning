from ctypes import c_double

a = "bramm"
b = 90
c = 4.21412
d = False
e = complex(2, 6)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(e)
print(type(e))

# bisa ambil dari C

f = c_double(10.5)
print(type(f))

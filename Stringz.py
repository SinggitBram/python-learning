print('domz de\'guud')
print('g\'day')
print("C:\\user\\domz")
print("ini\ttab jauh")
print("ini \bjadi deketan")
print("baris1 \nbaris2")  # ini LF untuk macos linux
print("baris1 \rbaris2")  # ini CR dah lama
print("baris1 \r\nbaris2")  # ini CRLF untuk windows

# string literal menggunakan raw string
print(r"C:\new folder")
print(r"""
Nama: Domz
kelas: 9Z
web: dom.com
""")
print("""
Nama: Domz
kelas: 9Z
web: dom.com
""")
print(5*"wkwk")

text = "pisang goreng"
print(text[0:6])
print(text[-4])
print(text[7:])

a = "                 hello world"
print(a[7:])
print(a[-5:-2])
print(len(a))  # untuk tau length
print(a.strip())  # trim
print(a.replace("o", "z"))

texzz = "the rain in bandung"
vv = "ain" in texzz
zz = "ain" not in texzz
print(vv)
print(zz)

age = 30
tinggi = 170
txt = "my name bram my age {} {}"
print(txt.format(age, tinggi))

uang = 9000
hari = "minggu"
makanan = "steak"

txtt = "i want to pay {2} for {0} day {1}"
print(txtt.format(makanan, hari, uang))

lklk = 300
print(isinstance(lklk, int))

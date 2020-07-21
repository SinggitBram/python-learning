data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data2 = [100, 200, 300, 400, 500]
data2[1] = 829
data3 = data + data2

a = data[:]
a[0] = 9999999999999

print(a)
subdata = data[0]
subdata2 = data[-5]
subdata3 = data[2:5]
subdata4 = data[-3:]

# print(subdata)
# print(subdata2)
# print(subdata3)
# print(subdata4)
print(data3)

azc = range(7)
print(azc)


thislist = ["dog", "cat", "bird", "hamster", "fish","elephant","lion","tiger","mouse"]
thislist.append("apple")
thislist.insert(1,"orange")
thislist.pop()
del thislist[4]
# thislist.clear()

#bikin copy variabel
list2 = thislist.copy()
list3 = list(thislist)
list4 = thislist[:]

listxxx = ["naga"]
for i in list4:
    listxxx.append(i)

ppp = [3,5,8]
lll = ["Satu","Dua","Tiga"]
ppp.extend(lll)
print(ppp)

print(thislist)
print(list2)
print(list3)
print(list4)
print(listxxx)

# for i in thislist:
#     print(i)

# if "hamster" in thislist:
#     print("ada")

#buat list baru
thelist = list(("apel","pisang","mangga"))
print(thelist)
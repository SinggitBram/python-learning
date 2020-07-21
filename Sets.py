thisset = {"apel","jeruk","anggur","mangga","pisang"}

# for i in thisset:
#     print(i)

# print("apel" in thisset)


# nambah 1 item
thisset.add("durian")

#nambah banyak item
thisset.update(["anjing","kucing","semut"])

# untuk hapus bisa remove ato discard
thisset.discard("kucing")

x=thisset.pop()

set2 = {3,6,3,7,1,8,8,8,8}
print(set2)

set3 = thisset.union(set2)

thisset.update(set2)

print(set3)
print(x)
print(thisset)
inituple = ("apel","semangka","melon","jeruk")
diubah = list(inituple)
diubah[2] = "kiwi"
inituple = tuple(diubah)

print(inituple)

thistuple = ("cumasatu",)
# del thistuple

print(type(thistuple))

tuple3 = inituple + thistuple

print(tuple3)
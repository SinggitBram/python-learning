thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "red"
thisdict["year"] = 2018
thisdict.pop("model")

# x = thisdict["model"]
# y = thisdict.get("year")
# print(x)
# print(y)

# panggil key 1 per 1
for i in thisdict:
    print(i)

# panggil value 1 1
for j in thisdict.values():
    print(j)

# panggil 2 2 nya
for k, l in thisdict.items():
    print(k, l)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


mydict = thisdict.copy()
mydict = dict(thisdict)
print(mydict)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

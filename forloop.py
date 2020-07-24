fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in range(2, 60, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty", "small","medium"]

for x in adj:
  for y in fruits:
    print(x, y)

for i in range(1,len(adj)-1):
    print(adj[i])

for x in [0, 1, 2]:
  pass
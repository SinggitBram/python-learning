i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# continue untuk ngeskip yg itu tp lanjut loopnya
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
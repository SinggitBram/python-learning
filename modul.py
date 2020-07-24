import platform
import mymodule as mx
from mymodule import person1

# a = mymodule.person1["age"]
# print(a)

# mymodule.greeting("Jonathan")

a = mx.person1["age"]
print(a)

# platform adalah buildt in modul
x = platform.system()
print(x)

# x = dir(platform)
# print(x)

print (person1["age"])
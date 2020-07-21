if 5 > 3:
    print("betul")

x = "awesome"
z = "lets go"


def myfunc():
    global y  # supaya var y jadi global ga local
    global z  # untuk ngubah var global dr dalem function
    y = "fabulous"
    x = "fantastic"
    z = "baruuuu"
    print("Python is " + x)


myfunc()
print(y)
print(z)

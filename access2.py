a=1000
def f1():
    global a
    a=2000
    print(a)

def f2():
    print(a)
f2()
f1()
print(a)
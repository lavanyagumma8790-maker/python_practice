def fun(*args,**kwargs):
   
    print("**kwargs")
    for key , value in kwargs.items():
        print(f"{key}={value}")
    print("*args")
    for arg in args:
        print(arg)
fun("hey", "lavanya",name="lavanya",age=20)
a=3
if a<0:
    print("factorial is not defined for negative numbers")
else:
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print("factorial of a give number is:",fact)
a=12345
sum=0
while a>0:
    last=a%10
    sum+=last
    a=a//10
print("sum of digits is:",sum)
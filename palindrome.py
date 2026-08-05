a = 121

reverse = 0

while a > 0:
    last = a % 10
    reverse = reverse * 10 + last
    a = a // 10

if  reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
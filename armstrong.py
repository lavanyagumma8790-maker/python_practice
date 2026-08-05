a = 153
arm = a
count = 0

while a > 0:
    last = a % 10
    count += last ** 3
    a = a // 10

if count == arm:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
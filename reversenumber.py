a = 12345
reverse = 0

while a > 0:
    last = a % 10
    reverse = reverse * 10 + last
    a = a // 10

print("Reversed number:", reverse)
a = [-1,2,-3,-4,5,6]

pos = 0
neg = 0

for i in a:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1

print("Positive numbers are:", pos)
print("Negative numbers are:", neg)
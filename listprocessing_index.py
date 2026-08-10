a = [12, 7, 4, 9, 6, 3]

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i] // 2
    else:
        a[i] = a[i] * 2

print(a)
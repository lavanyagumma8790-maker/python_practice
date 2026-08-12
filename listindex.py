a = [12, 5, 8, 15, 3, 10]

for i in range(0,6):
    if a[i] % 2 == 0:
        a[i] = a[i] + i
    else:
        a[i] = a[i] - i

print(a)
a = [16, 17, 4, 3, 5, 2]

leaders = []
max_right = a[-1]

leaders.append(max_right)

for i in range(len(a) - 2, -1, -1):
    if a[i] > max_right:
        leaders.append(a[i])
        max_right = a[i]

leaders.reverse()

print("Leaders:", leaders)
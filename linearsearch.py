lst = [1, 34, 56, 32, 56, 87]

tar = int(input("Enter element to be searched: "))

found = False

for i in lst:
    if i == tar:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
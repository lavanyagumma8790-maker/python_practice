a = input("Enter a string: ")
count = 0

for i in a:
    if i in "aeiouAEIOU":
        count += 1

print("Number of vowels in a string is:", count)
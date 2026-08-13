a = input().split()
longest=0
word=0
print(a)
for char in a:
        length= len(char)
        if length>longest:
            longest=length
            word=char

print("longest word is:",word)
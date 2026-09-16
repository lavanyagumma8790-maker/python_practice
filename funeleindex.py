def indexl(lst,tar):
  for i in range(len(lst)):
    if lst[i]==tar:
      return i
  return -1
lst=[1,2,5,36,7,8]
tar=int(input("enter element to be searched:"))
temp=indexl(lst,tar)
if temp:
  print(f"element found at index: {temp}")
else:
  print("element not found")
      
      
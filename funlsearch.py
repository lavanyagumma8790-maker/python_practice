def linear(lst,tar):
  for i in lst:
    if i==tar:
      return True
  return False
lst=[1,67,45,26]
tar=int(input("enter element to be searched:"))
temp=linear(lst,tar)
if temp:
  print("found")
else:
  print("not found")

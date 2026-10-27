def small(a):
  
  min1=a[0]
  sec_min=a[0]
  for i in a:
    if i < min1:
      sec_min=min1
      min1=i
  print(f'minimum element in the list is:{min1}')
  for i in a:
    if i> sec_min and i< min1:
      sec_min=i
  print(f"second minimum element is:{sec_min}")

a=[12,45,7,89,34]
small(a)

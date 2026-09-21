def evenodd(a):
  counteven=0
  countodd=0
  for i in a:
    if i%2==0:
     
      counteven+=1
      

  for i in a:
    if i%2 != 0:
     
      countodd+=1
  print("no.of odd numbers are:",countodd)
  print("number of even numbers are:",counteven)
a=[10,15,22,7,8]
evenodd(a)
      
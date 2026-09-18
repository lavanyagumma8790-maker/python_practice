def displayresults(marks):
  high=marks[0]
  for i in marks:
    if i>high:
      high=i
  print(f"Highest marks are: {high}")
  low=marks[0]
  for i in marks:
    if i < low:
      low=i
  print(f"Lowest marks are: {low}")
 
  total = 0
  for i in marks:
      total = total + i

  average = total / len(marks)
  print(f"Average marks are: {average}")


marks = [78, 85, 92, 67, 88]
displayresults(marks)
  




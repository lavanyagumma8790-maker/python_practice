class Employee:
  def __init__(self,ename,esalary):
    self.ename=ename
    self.esalary=esalary
  def display(self):
    print(f"employee name: {self.ename}\nemployee salary:{self.esalary}")
y=Employee("lavanya",50000)
y.display()

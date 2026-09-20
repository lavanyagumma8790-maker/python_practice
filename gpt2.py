class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
      print(f"Area is:{self.length*self.breadth}")
  def perimeter(self):
        print(f"Perimeter of Rectangle is:{2*(self.length+self.breadth)}")
y=Rectangle(2,3)
y.area()
y.perimeter()
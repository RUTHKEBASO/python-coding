# class to do ....
class Rectangle:
  def __init__(self,length,width):
   self.length = length
   self.width=width
  def area(self):
    return self.length*self.width


  def perimeter(self):
        return self.length+self.width


  r=Rectangle(6,5)
  print(r.area())
  print(r.perimeter())
  r.perimeter()
  r.area()


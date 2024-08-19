class square ():

  def __init__(self,num) :
    self.num=num
  
  def square(self):
    print(f"square of {self.num} is {self.num*self.num}")
  
  def square_root(self):
    print(f"square root of {self.num} is {round(self.num**0.5)}")


num = square(16)
num.square()
num.square_root()
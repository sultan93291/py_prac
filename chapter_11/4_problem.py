class Complex :
  def __init__(self,r,i)  :
    self.r=r
    self.i=i

  def __add__(self,c2):
    return Complex(self.r+c2.r , self.i + c2.i)
  
  def __mul__(self,c2):
    real_part= self.r * c2.r - self.i*c2.i
    imaginary_part= self.r * c2.i + self.i*c2.r
    return Complex(real_part,imaginary_part)
  
  def __str__(self) :
    return(f" {self.r} + {self.i}i")


com1= Complex(3,5)
com2= Complex(2,5)

print(com1+com2)
print(com1*com2)
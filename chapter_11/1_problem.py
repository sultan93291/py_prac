class two_d_Vector():
  
  def __init__(self,i,j) :
    self.i= i
    self.j = j
  
  def show(self):
    print(f"the 2d vetor is {self.i}i + {self.j}j ")



class three_d_Vector(two_d_Vector):

  def __init__(self,i,j,k):
    super().__init__(i,j)
    self.k = k

  def show(self):
    print(f"the 3d vetor is {self.i}i + {self.j}j + {self.k}k ")


twoD = two_d_Vector(5,7)
threeD = three_d_Vector(9,5,4)
twoD.show()
threeD.show()
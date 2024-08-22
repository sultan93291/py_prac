class Vector :
  def __init__(self,x,y,z)  :
    self.x=x
    self.y=y
    self.z=z

  def __add__(self,other):
    return Vector(self.x+other.x , self.y + other.y, self.z+ other.z)
  
  def __mul__(self,other):
    result = self.x *other.x + self.y *other.y + self.z *other.z
    return result
  
  def __str__(self) :
    return(f"  {self.x}i + {self.y}j + {self.z}k")
  


vec1 = Vector(5,9,12)
vec2 = Vector(12,8,7)
vec3 = Vector(3,8,4)


print(vec1+vec3)
print(vec3*vec2)
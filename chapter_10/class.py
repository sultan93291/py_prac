class employee:
  
  language="python"
  salary = 120000

  def __init__(self,name, age, language) :

    self.name= name
    self.age=age
    self.language= language
    

  def getInfo(self):
    print(f"your name is {self.name} and your age is {self.age} . and your salary is {2000000 if self.language=="c++" else self.salary }.your language was {self.language}")

  @staticmethod
  def greet():
    print("good night")


sultan= employee("abib",22,"javascript")
abib= employee("dipto",50,"c++")
sultan.getInfo()
sultan.greet()
abib.getInfo()
# print(sultan.language, sultan.salary)
# print(abib.language, abib.salary , abib.name)

class programmer():
  company = "microsoft.com"

  def __init__(self,name,age,salary,pin) :
    self.name=name
    self.age=age
    self.salary=salary
    self.pin=pin

  def getInfo(self):
    print(f"hey {self.name}. you're age is {self.age} . you work for {self.company}. And your salary is {self.salary} . your pin is {self.pin}. it's a confidential information.")

abib=programmer("Dipto",21,120000,2455)
sultan=programmer("abib",23,220000,2654)
abib.getInfo()
sultan.getInfo()

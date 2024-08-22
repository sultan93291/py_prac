class Employee():
  salary= 20000
  increment= 20
  

    
  @property 
  def count_salary_increment(self):
    salary_after_increment = (self.salary+ self.salary * (self.increment/100))
    print(f" salary incremented {salary_after_increment}bdt")
    return salary_after_increment
  
  @count_salary_increment.setter
  def count_salary_increment (self,salary):
    self.increment = ((salary/self.salary)-1)*100
    




employee = Employee()
employee.count_salary_increment=28000

print(employee.increment)
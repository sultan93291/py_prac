class Employee():
  
  def __init__(self,salary,increment) :
    self.salary= salary
    self.increment= increment
    print(f"your current salary is {salary} bdt")
    

  def count_salary_increment(self):
    salary_after_increment = self.salary /100 *self.increment
    print(f" salary incremented {salary_after_increment}bdt")
    return salary_after_increment
  

  def total_salary_after_increment(self):
    increment_amount = self.count_salary_increment()
    print(f"total salary after increment  is { self.salary + increment_amount} bdt")




employee = Employee(20000,20)
employee.total_salary_after_increment()

from random import randint

class ticket ():

  def __init__(self,trainNO) :
    self.trainNo = trainNO
    
  def book(self,fro,to):
    self.fro= fro
    self.to=to
    print(f"hey there your ticket no is {self.trainNo} your journey begins in  {self.fro} and your destination is {self.to}")

  def getStatus(self):
      print(f"Train no {self.trainNo} is running on time")

  def getFare(self,fro,to):
    self.fro= fro
    self.to=to
    print(f"ticket fare into {self.trainNo} . from {self.fro} to {self.to}. is{randint (500,2000)} bdt ")

train= ticket(15550)
bookTicket= train.book("Dhaka","Chittagong")
trainStatus= train.getStatus()
bookReturnTicket= train.getFare("Dhaka","Chittagong")

class animals():
  pass

class pets(animals):
  pass

class dog(pets):

  @staticmethod
  def bark():
    print("dog is bariking : bow bow ! ")

Dog= dog()
Dog.bark()
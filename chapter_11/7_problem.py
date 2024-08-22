class Vector :
  def __init__(self,list)  :
    self.list= list

  def __len__(self) :
    return(len(self.list))
  
  def get_items(self):
    for index , item in enumerate(self.list):
      print(f" item {item} is in {index} index")


vec1 = Vector([5,9,12,13,14,15,16,17,18,19])
vec1.get_items()
print(len(vec1))




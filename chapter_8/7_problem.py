list = ["sultan","sanjar","abib" ,"sanjida",'Harry']

def remove(list,word):
  nL= []
  for item in list:
    if not (item == word):
      nL.append(item.strip(word))
  return nL

word = input("Enter the word you want to remove : ")
removed_list= remove(list, word)
print(removed_list)
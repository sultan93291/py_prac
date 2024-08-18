p_1 = "subscribe "
p_2 = "make money"
p_3= "claim your reward"
p_4= "get your car"

comment = input("Enter your comment : ")

if( (p_1 in comment) or (p_2 in comment) or(p_3 in comment) or(p_4 in comment)):
  print("your're suspecious")

else:
  print(comment) 
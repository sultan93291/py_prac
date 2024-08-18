num_one = int(input("Enter The first number : "))
num_two = int(input("Enter The second number : "))
num_three = int(input("Enter The third number : "))
num_four = int(input("Enter The fourth number : "))


if(num_one > num_two and  num_one > num_three and num_one > num_four):
  print("number one is the biggest number",num_one)
elif(num_two > num_one and  num_two > num_three and num_two > num_four):
  print("number two is the biggest number",num_two)
elif(num_three > num_one and  num_three > num_two and num_three > num_four):
  print("number three is the biggest number",num_three)  
else:
  print("number four is the biggest number", num_four)  
num_one = int(input("Enter the first number : "))
num_two = int(input("Enter the second number : "))
num_three = int(input("Enter the third number : "))


def greatest (num_one, num_two, num_three):
  if(num_one>num_two and num_one >num_three):
    return num_one
  elif(num_two>num_one and num_two >num_three):
    return num_two
  else:
    return num_three
  

average_of_three = greatest(num_one, num_two, num_three)

print(f" greatest of three is {average_of_three}")
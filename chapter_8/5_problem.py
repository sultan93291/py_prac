num = int(input("Enter the number : "))

def pattern (num):
  if(num==0):
    return
  print("*" * num)
  pattern(num-1)

pattern(num)
# print(print_num)
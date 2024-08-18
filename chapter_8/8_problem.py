num = int(input("Enter the number you want to multiply : "))
def multiply(num):
  for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

multiply(num)

num = int(input("Enter your number : "))


for i in range (2, num):
  if(num%i)==0:
    print("number is not prime")
    break

else:
  print(f"number is prime {num}")
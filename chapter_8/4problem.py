num = int(input("Enter the number : "))

def sum (num):
  if(num==1):
    return 1
  else:
    return  sum(num-1)+ num 
  
sum_of = sum(num)

print(sum_of)

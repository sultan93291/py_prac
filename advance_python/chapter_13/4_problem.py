num_list = [1, 2, 3, 4, 5, 6,12,13,14,15,20]

for item in num_list:
  if(item%5==0):
    print(f" {item} is divisible by 5")


# another method 

def divisbleBy5(num):
  if(num%5==0):
    return True
  False

filtered_list = list(filter(divisbleBy5,num_list))

print(list(filtered_list))

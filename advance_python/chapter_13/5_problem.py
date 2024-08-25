from functools import reduce
num_list = [100,153,854,566,984,4646,745]


def greater(a,b):
  if(a>b):
    return a 
  return b

greater_num = (reduce(greater, num_list))

print(greater_num)
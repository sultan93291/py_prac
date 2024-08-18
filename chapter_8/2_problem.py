def f_to_c (f):
  return 5*(f-32)/9

f = int(input("Enter the temperature in f: "))
tem_in_c = f_to_c(f)
print(f"temperature in c is {round(tem_in_c) }° c")
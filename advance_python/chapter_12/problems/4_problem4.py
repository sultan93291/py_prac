a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

def sum(a,b):
  try:
    sum= a/b
    print(sum)
    return sum
  except ZeroDivisionError as e:
    print("inifinite")
    print(e)


sum(a,b)
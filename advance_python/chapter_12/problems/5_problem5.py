num = int(input("Enter a number : "))
table = [num*i for i in range(1,11)]

with open(f"tables/table{num}.txt","w") as f:
  f.write(str(f"Tabe of {num}: {table}"))


print(table)
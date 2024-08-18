
def generate_table(num):
  table=""
  for i in range(1,11):
    table += f"{num} x {i} = {i*num}\n"
    with open(f"tables/table{num}.txt","w") as f:
      f.write(table)

for i in range (1,21):
  generate_table(i)
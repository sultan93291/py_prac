with open("poem.txt","r") as f:
  poem_content = f.read()

with open("copy.txt","r") as f:
  copy_content = f.read()

if(poem_content == copy_content):
  print("both content are same")
else:
  print("both content are different")
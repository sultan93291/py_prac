f= open("poem.txt","r")

conetnt= f.read()

if ("twinkle" in conetnt):
  print("twinkle is in the poem")
else: 
  print("twinkle is not in the poem")
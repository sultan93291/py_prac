

with open("log.txt", "r") as f : 
  lines = f.readlines()
  
lines_no =1

for line in lines:    
  if("python "in line):
    print(f"python is avlaible. \n\tIn line : {lines_no}.")
    break
  lines_no +=1 

else: 
  print("python is not avilable")  



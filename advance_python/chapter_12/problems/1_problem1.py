try :
  with open("file.txt") as f:
    print(f.read())
except Exception as e:
  print(e)

try :
  with open("filex.txt") as f:
    print(f.read())
except Exception as e:
  print(e)

try :
  with open("filey.txt") as f:
    print(f.read())
except Exception as e:
  print(e)

print("Thank you !")
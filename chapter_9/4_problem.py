def chane_word():
  content= ""
  with open("donkey.txt","r") as f:
    content= f.read()
    if("donkey" in content):
      newCotnet= content.replace("donkey", "####")
      with open("donkey.txt","w") as f:
        f.write(newCotnet)
    else:
      print("no monkey found")

chane_word()
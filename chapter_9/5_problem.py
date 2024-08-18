list = ["donkey","monkey","sala","haramkhor"]


def chane_word():
  content=""
  with open("abuse.txt","r") as f:
    content= f.read()

    found = False

    for item in list:

      if item in content :
        found = True
        content= content.replace(item, "#" * len(item))
        with open("abuse.txt","w") as f:
          f.write(content)
    if(found):
      print("slungs found on your comments")
    else:
      print("slungs not found on your comments")


      
      



chane_word()
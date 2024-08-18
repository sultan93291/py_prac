import random

def game():
  print("You're playing the game...")
  score = random.randint(1,100)
  with open("hi_score.txt") as f : 
    hi_score= f.read()
    if( hi_score !="" ):
      hi_score=int(hi_score)
    else:
      hi_score=0 
  print(f"your score is {score}")
  if(score>hi_score):
    with open("hi_score.txt","w") as f: 
      f.write(str(score))
      print(f"congratulation you beat the last high score .\n New high score is {score}")
  return score

game()
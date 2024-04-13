import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == "stone" and user =="scissor"):
    return -1
    
  if(comp == "paper" and user =="stone"):
    return -1
    
  if(comp == "scissor" and user == "paper"):
    return -1

  return 1
    
options = ["stone", "paper", "scissor"]
comp = random.choice(options)
user = input("choose from Stone,paper and scissors: ")

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")

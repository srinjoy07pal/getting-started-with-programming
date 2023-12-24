import random

def get_choices():
  player_choice=input("Enter a choice (rock ,paper,scissors):")
  options=["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}
  return choices
  
def check_win(player,computer):
  print("You chose :"+player+ ",computer chose: "+computer)
  if player == computer:
    return "It's a tie!"
  elif player == "rock" and computer == "scissors": 
    return "You Won"
  elif player == "rock" and computer =="paper":
    return "You Lost"
  elif player == "paper" and computer =="rock":
    return "You Won"
  elif player == "paper" and computer =="scissors":
    return "You Lost"
  elif player == "scissors" and computer =="rock":
    return "You Lost"
  elif player == "scissors" and computer =="paper":
    return "You Won"
    
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

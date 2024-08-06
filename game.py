import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors) : ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  dict = {"player": player_choice, "computer": computer_choice}
  return dict


def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "rock smashes scissors! You win!"
    else:
      return "paper cover rock! You lose."
  elif player == "paper":
    if computer == "scissors":
      return "scissors cut paper! You lose."
    else:
      return "paper cover rock! You win!"
  else:
    if computer == "paper":
      return "scissors cut paper! You Win!"
    else:
      return "rock smashes scissors! you lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)

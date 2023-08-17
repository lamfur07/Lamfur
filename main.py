import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_name(player):
  if player not in ["rock", "paper", "scissors"]:
    return


def check_win(player, computer):
  print(f"You chose {player} and the computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif (player == "rock" and computer == "paper"):
    return f"{computer} wins!!"
  elif (player == "rock" and computer == "scissors"):
    return f"{player} wins!!"
  elif (player == "scissors" and computer == "rock"):
    return f"{computer} wins!!"
  elif (player == "scissors" and computer == "paper"):
    return f"{player} wins!!"
  elif (player == "paper" and computer == "rock"):
    return f"{player} wins!!"
  elif (player == "paper" and computer == "scissors"):
    return f"{computer} wins!!"
  else:
    return "Enter Correct Choice"


choice = get_choices()
response = check_name(choice["player"])
print(response)
print(check_win(choice["player"], choice["computer"]))

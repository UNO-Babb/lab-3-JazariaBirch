#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  
  play = "Y"
  while play == "Y":

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

    player = input("Choice (Rock,Paper,Scissors):")
    
    computor = random.choice (["Rock" , "Paper" , "Scissors"])
    if computor == "Rock":
      print("Opponent chose Rock:")
    if computor == "Paper":
      print("Opponent chose Paper")
    if computor == "Scissors":
      print("Opponent chose scissors")

    if player == computor :
      print("Tie")
      ties = ties + 1
    elif player == "Rock" and computor == "Scissors":
      print("You Win!:D")
      wins = wins + 1
    elif player == "Rock" and computor == "Paper":
      print("You Lose.D:")
      losses = losses + 1
    elif player == "Paper" and computor == "Rock":
      print("You Win!:D")
      wins = wins + 1
    elif player == "Paper" and computor == "Scissors":
      print("You Lose.D:")
      losses - losses + 1
    elif player == "Scissors" and computor == "Rock":
      print("You Lose.D:")
      losses = losses + 1
    elif player == "Scissors" and computor == "Paper":
      print("You Win!:D")
      wins = wins + 1

      
    play = input("play again? (y/n): ")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()

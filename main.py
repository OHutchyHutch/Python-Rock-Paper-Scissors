print("Made by Owen Hutchins. Check me out @ ohutchyhutch.com")
lose, win = "You lost!", "You win!"
score, draw, gameround = 0, 0, 0
while True:
  print("To begin, fill in the below information")
  rounds = int(input("How many rounds do you want this game to be out of? Recommended: 5    |    "))
  username = input("Username:  ")
  searchfile = open("accounts.csv","r")
  for line in searchfile:
    if username in line:
      print("Access Granted. You've won X many games")
      print("| -------------------------------------- |")
      print("|                                        |")
      print("|           ROCK PAPER SCISSORS          |")
      print("|           By: Owen Hutchins            |")
      print("|                                        |")
      print("| -------------------------------------- |")
      print("Rules:")
      print("Best out of " + str(rounds) + " wins.")
      print("Paper beats rock. Rock beats scissors. Scissors beats paper.")
      while True:
        print("")
        print("---------")
        rps = input("Rock, Paper, or Scissors?  ").lower()
        print("---------")
        print("")
        import random
        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        if rps == "exit":
          break
        #Player chose rock
        if rps == "rock":
          if computer == "paper":
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print(lose)
            gameround+=1
          elif computer == "scissors":
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print(win)
            gameround+=1
            score+=1
          else:
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print("Draw!")
            gameround+=1
            draw+=1
        #Player chose paper
        elif rps == "paper":
          if computer == "scissors":
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print(lose)
            gameround+=1
          elif computer == "rock":
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print(win)
            gameround+=1
            score+=1
          else:
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print("Draw!")
            gameround+=1
            draw+=1
        #Player chose scissors
        else:
          if computer == "rock":
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print(lose)
            gameround+=1
          elif computer == "paper":
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print(win)
            gameround+=1
            score+=1
          else:
            print("You Chose | Computer Chose")
            print(rps + " | " + computer)
            print("Draw!")
            gameround+=1
            draw+=1
        #Game End Check
        import math
        #If won enough games.
        if math.ceil(rounds/2) <= score:
          print("You've won the game!")
          print(score)
          stop = input("Press enter to exit.")
        #manual exit
        elif rounds == gameround:
          if math.ceil(rounds/2) > score and math.ceil(rounds/2) != draw:
            print("You've lost the game!")
            print(score)
            stop = input("Press enter to exit.")
          else:
            print("The game is a draw!")
            stop = input("Press enter to exit.")
        
    else:
      print("Your username was not found! Please create one!")
        
print("------------------------------------")
print("Rock, Paper, Scissors Account Setup")
print("------------------------------------")
while True:
  username = input("Pick a username:  ")

  print("Your account has been created!")
  text_file = open("accounts.txt","a")
  text_file.write(username)
  text_file.write("\n")
  text_file.close()

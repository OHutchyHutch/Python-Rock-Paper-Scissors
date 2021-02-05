print("------------------------------------")
print("Rock, Paper, Scissors Account Setup")
print("------------------------------------")
while True:
  username = input("Pick a username:  ")

  print("Your account has been created!")
  text_file = open("accounts.csv","a")
  text_file.write(username)
  text_file.write(",")
  #score
  text_file.write("0")
  text_file.write(",")
  #draws
  text_file.write("0")
  text_file.write(",")
  text_file.close()
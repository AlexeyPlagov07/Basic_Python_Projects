import random
#Computes the decision making behind the choices#
def decision():
  if u_c == "Rock":
    if r_c == "Paper":
      print("You Lose!")
    if r_c == "Scissors":
      print("You Win!")
  if u_c == "Paper":
    if r_c == "Rock":
      print("You Win!")
    if r_c == "Scissors":
      print("You Lose!")
  if u_c == "Scissors":
    if r_c == "Paper":
      print("You Win!")
    if r_c == "Rock":
      print("You Lose!")

#Creates a list of the three choices#
choices = ["Rock","Paper","Scissors"]
#Selects a random choice from the list#
r_c = random.choice(choices)


#asks user if they want to play# 
answer = input("Would you like to play?(yes/no): ")
#Makes a while loop that says that as long as the user states "yes", the progra, will run#
while answer == "yes":
  #asks user for input on choice#
  u_c = input("Enter choice(Rock, Paper, Scissors): ")
  print("Opponent Chose", r_c)
  #if the choices are the same it returns a Tie#
  if u_c == r_c:
    print("You Tied!")
  else:
    decision()
  answer = input("Would you like to play again?(yes/no): ")
#prints the text and exits the command#
print("Thank you for playing!")
exit()

import random
#makes a dictionary of all 4 of the choices and the range of numbers that you can chose from#
choices = {"beginner" : list(range(1,11)), "intermediate" : list(range(1,51)), "hard" : list(range(1,101)), "impossible" : list(range(1,1001))}

#establishes "try again" variable#
try_again = "yes"

#makes a loop that while the user prints yes, the game will continue#
while try_again == "yes":
  #asks user for the difficulty#
  choice = input("Beginner = 1-10, Intermediate = 1-50, hard = 1-100, impossible = 1-1000 \nChoose Dificulty(beginner/intermediate/hard/impossible): ")
  #brings up the number range based on the user's difficulty choice#
  u_c = choices[choice]
  #random number is selected#
  random_choice = random.choice(u_c)
  #input where user guesses number#
  user_guess = input("Guess number: ")
  #boolean that determines if the guess was right or wrong#
  if user_guess == random_choice: 
    print("Congratulations you got it right!")
  else:
    print("You got it wrong. \nthe correct number was",random_choice)
    try_again = input("Would you like to play again?(yes/no): ")
  

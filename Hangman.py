import random
#establishes a word bank#
word_bank = ["apple", "banana", "pear", "peach", "watermelon", "lemon", "lime", "orange", "apricot", "blueberry", "blackberry", "currant", "cantaloupe", "cherry", "coconut", "cranberry", "plum", "elderberry", "fig", "grape", "grapefruit", "kiwi", "mango", "pineapple", "raspberry", "strawberry", ]
#defines which one of the limbs will be deleted from the list based on how many lives are left#
def hangman_limb(live):
  if live == 5:
    hang_man[46] = " "
  elif live == 4:
    hang_man[48] = " "
  elif live == 3:
    hang_man[35] = " "
  elif live == 2:
    hang_man[37] = " "
  elif live == 1:
    hang_man[36] = " "
  elif live == 0:
    hang_man[26] = " "
#choses random word from list#
rand_word = random.choice(word_bank)
#establishes lives#
lives = 6
#makes the word a number of blanks for the user to guess#
word_list = ['_']
#makes the number of blanks equal to the number of letters in the word#
word_list = word_list * len(rand_word)
#makes the list combined into a list#
word_outline = (''.join(word_list))
#this is the hangman that is in list form#
hang_man = list("_______ \n/      | \n|      o \n|     /|\\ \n|     / \\")
#makes the hangman list into a string for the user to see#
print(''.join(hang_man))
#prints the word outline#
print(word_outline)
#makes a loop that says as long as the user is still guessing the word and that still has lives, the user plays#
while lives > 0 and word_outline != rand_word:
   #makes the user guess a letter#
  user_guess = input("Guess a letter: ")
  #sees if the letter is in the word#
  if user_guess in rand_word:
    
    #algorithm that sees in which indexes the letters are#
    positions = ([pos for pos, char in enumerate(rand_word) if char == user_guess])
    #for every position it is in the list, it replaces the blank with the letter that the user imputed#
    for i in range(len(positions)):
      
      
      word_list[positions[i]] = user_guess
  #if the letter is not in the word, it denies that it is in the word and decreases a life and completes the fucntion that takes away the limbs of the hangman#
  elif user_guess not in rand_word:
    print("That letter is not in the word")
    lives = lives - 1
    hangman_limb(lives)


    #combines the hangman into what the user should see to update the hangman due to the incorrect letter##
    print(''.join(hang_man))
  #prints the updated word outline with the correct guessed letters in the spots#
  word_outline = (''.join(word_list))
  print(word_outline)
else:
  #says the if the word is fully guessed, it prints the message that you guessed the word#
  if word_outline == rand_word:
    print("You guessed the word!")
  #prints you lost lives if the lives = 0#
  elif lives == 0:
    print("You lost all your lives. :(")

  
      

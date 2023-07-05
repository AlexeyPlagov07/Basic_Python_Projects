#creates an empty dictionary to act as a phonebook#
my_phonebook = {}
#creates a function to add a name to the book#
def add_item(x, y):
  my_phonebook.update({x : y})
#creates a function to delete a name from the book#
def delete_item(x):
  my_phonebook.pop(x)
#creates a function to view the list#
def view_list():
  print(my_phonebook)
#creates a function to delete the whole list#
def clear_list():
  my_phonebook.clear()
#sets a constant choice of "yes"#
choice1 = "yes"

#Sets a loop that will always run unless yu type exit and it forces it to stop#
while choice1 == "yes":
  #asks user what choice they want and it lists it for them#
  user_choice = input("1:Add item to phonebook \n2:Delete item from phonebook \n3:View phonebook \n4:Clear phonebook \nor ""exit"" to exit \nWhat is your choice?: ")
  #creates a function of what all the choices do and the loops where they will repeate untill you say no more#
  def choice():
    if user_choice == "1":
      add_choice = "yes"
      while add_choice == "yes":
        #user input for the person's name#
        p_name = input("Enter the person's name: ")
        #user input for the person's number#
        phone_num = input("Enter the person's number: ")
        add_item(p_name, phone_num)
        add_choice = input("Would you like to add another person?: ")
    
    elif user_choice == "2":
      delete_choice = "yes"
      while delete_choice == "yes": 
        #user input for the person's name#
        p_name = input("Enter the person's name: ")
        delete_item(p_name)
        delete_choice = input("Would you like you like to delete another person?: ")
    
    elif user_choice == "3":
      view_list()
    
    elif user_choice == "4":
      clear_list()
    elif user_choice == "exit":
      #brute exits the program#
      exit()
  choice()

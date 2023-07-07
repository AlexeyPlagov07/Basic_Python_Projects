#creates empty list#
mylist = []

#checks if item is in the list#
def item_checker():
  item_check = input("Check item in list: ")
  if item_check in mylist:
    print("yes")
  else:
    print("no")
#user picks what they want to add and they add the item to the list and then asks them if they want to do so more#
def list_add():
  add_list = input("What would you like to add?: ")
  add_list_order = int(input("In what place would you like to add the item?: "))
  index1 = add_list_order - 1
  mylist.insert(index1, add_list)
#deletes a certain iem of the list which the user picks#
def list_delete():
  remove_item = input("What item would you like to remove?: ")
  mylist.remove(remove_item)
#lets the user view the full list and prints arrows in front of them#
def full_list():
  for i in mylist:
    t = 0
    t = t + 1
    print("->" + i)
#clears the full list#
def clear_list():
  mylist.clear()

#sets the vaue of menu option to yes which helps begin the loop#
menu_option = "yes"
#loop which helps keep the list running#
while menu_option == "yes":
  print("Add item to list(1)\nDelete item from list(2)\nCheck if item in list(3)\nPrint full list(4)\nClear list(5)")
  menu_selection = int(input("Enter Selection: "))


#runs the functions when the right selection is made based on the question#
  if menu_selection == 1:
    add_list1 = "yes"
    while add_list1 == "yes":  
      list_add()
      add_list1 = input("Would you like to add anything else?: ")
  if menu_selection == 2:
    remove_list = "yes"
    while remove_list == "yes":
      list_delete()
      remove_list = input("Would you like to remove anything else?: ")
  if menu_selection == 3:  
    option = "yes"
    while option == "yes":
      item_checker()
      option = input("Want to ask again?: ")
  if menu_selection == 4:
    full_list()
  if menu_selection == 5:
    clear_list()
  #restarts the variable
  menu_option = input("Go back to main menu?: ")

#Creating Functions Defining operations#
def add(x, y):
  return(x + y)
def sub(x, y):
  return(x - y)
def mult(x, y):
  return (x * y)
def div(x, y):
  return (x / y)

#making statement for selection a function instead of writing it in the code#
def choice_selector():
  if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
  elif choice == "2":
    print(num1, "-", num2, "=", sub(num1, num2))
  elif choice == "3":
    print(num1, "*", num2, "=", mult(num1, num2))
  elif choice == "4":
    print(num1, "/", num2, "=", div(num1, num2))
  


#To not repeat the choice selection, establish the choice as '1' to bypss first while loop#
choice = '1'
#Repeats choice selection if the choice is not 1,2,3,4#
while choice != ('1','2','3','4'):
  choice = input("Enter operation(1:Add 2:Sub. 3:Mult. 4:Div. or ""EXIT"" to exit): ")
  if choice in ('1','2','3','4'):
    #number selection#
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
      
    choice_selector()
  elif choice == "EXIT":
    exit()
  else:
    print("Selection Error. Try again.")

import random
#states the different choices#
u_c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l_c = 'abcdefghijklmnopqrstuvwxyz'
numbs = '1234567890'
symbs = '!@#$%&?[]{}/'
#makes a string of all the characters named alphabet#
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&?[]{}/'
#asks user about the length of the passwords and the quantity#
u_c1 = int(input("Chose how long your password will be: "))
u_c2 = int(input("How many passwords do you want?: "))

#Calculates remainder to see how many more characters to add#
remain = u_c1 % 4
#the 'length' attribute is for dividing the password equally into the 4 different categories then adding the remainder from the large pool#
length = int(u_c1 / 4)


  
  



#the first loop is to see how many passwords are needed to be generated#
for i in range(u_c2):
  l = []
  
  #the second loop is to see how many characters are in the passwords#
  for i in range(length):
    x = random.choice(u_c)
    y = random.choice(l_c)
    z = random.choice(numbs)
    a = random.choice(symbs)
  
  
    l.append(x)
    l.append(y)
    l.append(z)
    l.append(a)
  #this loop is for adding the remaining characters
  for i in range(remain):
    l.append(random.choice(alphabet))

  #this adds all the characters in the lists and makes it a string#
  print(''.join(l))





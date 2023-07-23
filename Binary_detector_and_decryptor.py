#user input for ecrypted data#
e_c = encrypted_message = list(input("Enter encoded message: "))
#creates empty list#
x = []
decrypt_list = []
#appends the numbers in the user input to a list x which is determined by wether the number is a 1 or a 0#
for i in e_c:
  
  if i == "1":
    x.append(i)
  elif i == "0":
    x.append(i)
#joins the two lists and then compares them to see if the number is binary#
e_c = ''.join(e_c)
x = ''.join(x)
if x == e_c:
  print(x, "is a binary number!")
  #if the number is binary, it flips the number and for the index, the index becomes the 2 to the power of the index which determins the number based on the position of the 1 in the binary#
  x = len(list(e_c))
  #flips the binary number#
  e_c = e_c[::-1]
  for i in range(x):
    if e_c[i] == "1":
      #print(i, "<--")
      num_fragment = 2 ** i
      #print(num_fragment)
      decrypt_list.append(num_fragment)
  #finds the final number#
  decrypted_num = sum(decrypt_list)
  print("The decrypted number is", decrypted_num)
    

else:
  print("Not a binary number! :(")


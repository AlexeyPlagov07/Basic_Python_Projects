#encoded_message = input("Enter the encoded massage: ")
#reads the file and sets it to the data variable#
with open('filefile.txt', 'r') as file:
  data = file.read().replace('\n', '')
#prints the encoded message#
print("The encoded message is", data)
#sets the alphabet#
alphabet = list("abcdefghijklmnopqrstuvwxyz_")
#creates list for the characters to append to#
decoded_message = []
#splits the string into a list based on the numbers split by spaces#
B = [int(x) for x in data.split()]
#converts the numbers to the letters based on placement#
for i in B:
  x = (alphabet[i - 1])
  decoded_message.append(x)
#combines the list into a final string#
decoded_message1 = (''.join(decoded_message))
#prints the decoded message#
print("The decoded message is", decoded_message1)

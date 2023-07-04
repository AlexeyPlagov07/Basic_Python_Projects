import time
#sets user_input to tell the code how long the timer will be#
h = int(input("Enter time.(hours): "))
m = int(input("Enter time.(minutes): "))
s = int(input("Enter time.(seconds): "))
#a basic function that prints the result out in a formated sentence for the user to see#
def return1():
  print(h, "hours :", m, "minutes :", s, "seconds left")
#A loop that will run until all the values equal zero#
while (int(h) > -1) and (int(m) > -1) and (int(s) >= 0):
  
  #adds to the formallity of the code. If the length of the number is 1, then it will add a zero ex: 3 -> 03#
  if len(str(h)) < 2:
    h = (str(h).zfill(2))
  if len(str(m)) < 2:
    m = (str(m).zfill(2))
  if len(str(s)) < 2:
    s = (str(s).zfill(2))
    
  
  #These nested ifs decrease the number of hours when the minutes hit zero, also resest the seconds at 59#
  if int(m) == 0:
    if int(s) == 0:
      if int(h) > 0:
        return1()
        h = (str(int(h) - 1)).zfill(2)
        m = 59
        s = 59
        time.sleep(1)
  #These nested ifs subtract a minute when the seconds equal zero and reset the seconds to 59#
  if int(s) == 0:
    if int(m) > 0:
      
      return1()
    
      m = (str(int(m) - 1)).zfill(2)
      s = 59
      time.sleep(1)
  return1()
  #makes the seconds go down every second#
  time.sleep(1)
  s = int(s) - 1

  

#makes an else statement for the while loop that says when it is done, the code prints "Done!" and force exits#
else:
  print("Done!")
  exit()

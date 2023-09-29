list = [1,5,3,8,12,2,16,9,35,23,1,-1,54,1004,546]

for i in range(len(list)):
  for j in range(len(list)):
    if list[i] > list[j] and i < j:
      #Switches the positions of the items in the lists# 
      #if the first one is bigger but index is smaller#
      list[i], list[j] = list[j], list[i]
print("Sorted list using Bubble Sort: \n", list)

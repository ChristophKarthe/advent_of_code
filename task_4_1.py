import re

textfile = open('advent_of_code/input_4.txt','r')

# horizontal list creation
horizontal_list = textfile.read().split("\n")

# vertical list creation
vertical_list = []
for i in range(0,len(horizontal_list[0])):
    addingstring = ""
    for j in range(0, len(horizontal_list)):
        addingstring += horizontal_list[j][i]
    vertical_list.append(addingstring)

# diagonal list creation
diagonal_list = []
for i in range(0,(len(horizontal_list[0])-2)):
    addingstring = ""
    for j in range(-1, -(len(horizontal_list)),-1):
        # if i + abs(j) >= 140:
        #     break
        print(i)
        print(j)
        addingstring += horizontal_list[j][i+j]
    diagonal_list.append(addingstring)
for i in range(0,len(horizontal_list[0])-2):
    addingstring = ""
    for j in range(0, len(horizontal_list)):
        if i + j >= 140:
            break
        print(i)
        print(j)
        addingstring += horizontal_list[j][i+j]
    diagonal_list.append(addingstring)
print(diagonal_list)
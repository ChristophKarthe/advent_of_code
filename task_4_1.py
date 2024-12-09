import re

textfile = open('advent_of_code/input_4.txt','r')
sum = 0
# define xmascount
def xmascount(string):
    founditems = re.findall("XMAS", string)
    founditems2 = re.findall("SAMX", string)
    return (len(founditems) + len(founditems2))
def xmassum(list1):
    sum = 0
    print(list1)
    for i in range(0,len(list1)):
            sum += xmascount(list1[i])
    return sum
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
for i in range(3,(len(horizontal_list[0]))):
    addingstring = ""
    for j in range(-1, -(len(horizontal_list)),-1):
        if i + j < 0:
            break
        addingstring += horizontal_list[j][i+j]
    diagonal_list.append(addingstring)
for i in range(0,len(horizontal_list[0])):
    addingstring = ""
    for j in range(0, len(horizontal_list)):
        if i + j >= 140:
            break
        addingstring += horizontal_list[j][i+j]
    diagonal_list.append(addingstring)
# other direction diagonal list creation
diagonal_list2 = []
for i in range(2,(len(horizontal_list[0]))):
    addingstring = ""
    for j in range(0, len(horizontal_list)):
        if i - j < 0:
            break
        addingstring += horizontal_list[j][i-j]
    diagonal_list2.append(addingstring)
for i in range(1, len(horizontal_list)):
    addingstring = ""
    for j in range(-1, -(len(horizontal_list[0])),-1):
        if i + abs(j) >= 141:
            break
        addingstring += horizontal_list[i + abs(j)-1][j]
    diagonal_list2.append(addingstring)
superlist = [horizontal_list, vertical_list, diagonal_list, diagonal_list2]
for items in superlist:
    sum += xmassum(items)
print(sum)
# Imports
import math

# Arrays befüllen
textfile = open('./input_5.txt','r')
array1 = textfile.read().split("\n")
array2 = []
k = -1
for i in range(-1,-len(array1),-1):
    if len(array1[k]) > 5:
        array2.append(array1[k])
        array1.pop(k)
        k += 1
    k -= 1

array1.pop(-1)
array1new = []
array2new = []
for elements in array1:
    array1new.append(elements.split("|"))
for elements in array2:
    array2new.append(elements.split(","))
array1 = array1new
array2 = array2new

# mit den Arrays Arbeiten
addingarray = []
sum = 0
for elements in array2:
    superIsSafe: bool = True
    for element in array2[array2.index(elements)]:
        rulearray = []
        for items in array1:
            if element == array1[array1.index(items)][1]:
                rulearray.append(array1[array1.index(items)][0])
        for i in range(array2[array2.index(elements)].index(element)+1, len(array2[array2.index(elements)])):
            isSafe: bool = True
            for items in rulearray:
                if array2[array2.index(elements)][i] == items:
                    isSafe = False
                    break
            else:
                continue
            superIsSafe = isSafe
            break

    if superIsSafe:
        halfindex = math.ceil(len(elements)/2)-1
        addingarray.append(array2[array2.index(elements)][halfindex])
for elements in addingarray:
    sum += int(elements)
print(sum)
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
array1.reverse()
array2.reverse()
# mit den Arrays Arbeiten
addingarray = []
sum = 0
for elements in array2:
    superIsSafe: bool = True
    copyelements = elements
    for element in array2[array2.index(elements)]:
        rulearray = []
        for items in array1:
            if element == array1[array1.index(items)][1]:
                rulearray.append(array1[array1.index(items)][0])
        else:
            for i in range(copyelements.index(element)+1, len(copyelements)):
                isSafe: bool = True
                smallRuleArray = []
                for items in array1:
                    if element == array1[array1.index(items)][0]:
                        smallRuleArray.append(array1[array1.index(items)][1])
                for items in rulearray:
                    if copyelements[i] == items:
                        isSafe = False
                        copyelements[i], copyelements[copyelements.index(element)] = copyelements[copyelements.index(element)], copyelements[i]
                        for i in range(0, copyelements.index(copyelements[i])-1):
                            isSafe: bool = True
                            for items in smallRuleArray:
                                if copyelements[i] == items:
                                    isSafe = False
                                    copyelements[i], copyelements[copyelements.index(element)] = copyelements[copyelements.index(element)], copyelements[i]
                                    break
                            if isSafe == False : superIsSafe = isSafe 
                        break
                if isSafe == False : superIsSafe = isSafe
    if not superIsSafe:
        halfindex = math.ceil(len(copyelements)/2)-1
        addingarray.append(copyelements[halfindex])
for elements in addingarray:
    sum += int(elements)
print(sum)
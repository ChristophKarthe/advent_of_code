# Imports
import math
import operator
# Arrays befüllen
textfile = open('./input_5_example.txt','r')
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
for elements in array1:
    dic = {}
    dic[elements[0]] = 0
for elements in array1:
    dic[elements[0]] += 1
copyarray1 = []
for elements in array1:
    copyarray1.append(max(dic.items(), key=operator.itemgetter(1))[0])
    dic.pop(max(dic.items(), key=operator.itemgetter(1))[0])
array1 = copyarray1
print(array1)
def checkarray(elements, array1):
    superIsSafe: bool = True
    for element in elements:
        rulearray = []
        for items in array1:
            if element == array1[array1.index(items)][1]:
                rulearray.append(array1[array1.index(items)][0])
        for i in range(elements.index(element)+1, len(elements)):
            isSafe: bool = True
            for items in rulearray:
                if elements[i] == items:
                    isSafe = False
                    break
            else:
                continue
            superIsSafe = isSafe
            break
    return superIsSafe
# mit den Arrays Arbeiten
addingarray = []
sum = 0
for elements in array2:
    if not checkarray(elements, array1):
        dic = {}
        for element in elements:
            dic[element] = 0
        for items in array1:
            if array1[array1.index(items)][0] in dic.keys() and array1[array1.index(items)][1] in dic.keys():
                print(items)
                add = dic[array1[array1.index(items)][1]]
                dic[array1[array1.index(items)][0]] += add + 1
        copyelements = []
        print(dic)
        for element in elements:
            copyelements.append(max(dic.items(), key=operator.itemgetter(1))[0])
            dic.pop(max(dic.items(), key=operator.itemgetter(1))[0])
        halfindex = math.ceil(len(copyelements)/2)-1
        addingarray.append(copyelements[halfindex])
        print(copyelements)

for elements in addingarray:
    sum += int(elements)
print(sum)
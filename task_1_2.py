textfile = open('advent_of_code/input_1.txt','r')
list = textfile.read().split()
list1 = []
list2 = []
similarityscore = 0
for i in range(0,len(list)):
    if (i % 2) == 0:
        list1.append(list[i])
    else:
        list2.append(list[i])
list1.sort()
list2.sort()
for i in range(0,len(list1)):
    multiplier = 0
    for j in range(0,len(list2)):
        if int(list1[i]) == int(list2[j]):
            multiplier += 1
    similarityscore += int(list1[i]) * multiplier
print(similarityscore)
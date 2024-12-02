textfile = open('advent_of_code/input_day_1_1.txt','r')
list = textfile.read().split()
list1 = []
list2 = []
for i in range(0,len(list)):
    if (i % 2) == 0:
        list1.append(list[i])
    else:
        list2.append(list[i])
list1.sort()
list2.sort()
overallsum = 0
for i in range(0,len(list1)):
    sum = int(list1[i]) - int(list2[i])
    if sum < 0:
        sum = abs(sum)
    overallsum += sum
print(overallsum)
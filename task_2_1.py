textfile = open('advent_of_code/input_2.txt','r')
list = textfile.read().split("\n")
safereports = 0
for i in range(0,len(list)):
    list1 = []
    for x in list[i].split():
        x = int(x)
        list1.append(x)
    ascending = 0
    descending = 0
    k = 1
    for j in range (0,len(list1)-1):
        a = abs(list1[j]-list1[k])
        if list1[j] <= list1[k] and a <= 3 and a > 0:
            ascending += 1
        elif list1[j] >= list1[k] and a <= 3 and a > 0:
            descending += 1
        k += 1
    if ascending == (len(list1)-1) or descending == (len(list1)-1):
        print(list1)
        safereports += 1
print(safereports)
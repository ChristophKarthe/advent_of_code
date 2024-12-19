import re

textfile = open('./input_4.txt','r')
sum = 0

def xmascount(string):
    founditems = re.findall("MASMAS", string)
    founditems2 = re.findall("SAMSAM", string)
    founditems3 = re.findall("MASSAM", string)
    founditems4 = re.findall("SAMMAS", string)
    return (len(founditems) + len(founditems2) + len(founditems3) + len(founditems4))

def xmassum(list1):
    sum = 0
    print(list1)
    for i in range(0,len(list1)):
            sum += xmascount(list1[i])
    return sum

horizontal_list = textfile.read().split("\n")


list1 = []
for i in range(0, len(horizontal_list)-2):
    for j in range(0,len(horizontal_list[0])-2):
        addingstring = ""
        for k in range(0,3):
            addingstring += horizontal_list[i+k][j+k]
        for k in range(0, -3, -1):
            addingstring += horizontal_list[i+abs(k)][j+k+2]
        list1.append(addingstring)
print(xmassum(list1))
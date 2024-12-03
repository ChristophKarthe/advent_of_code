import re

textfile = open('advent_of_code/input_3.txt','r')
list = textfile.read().split("m")
pattern = r"[u][l][(]\d+[,]\d+[)]"
pattern2 = r"\d+"
sum = 0
for i in range(0,len(list)):
    validate = re.search(pattern, list[i])
    if validate:
        mlist = re.findall(pattern2, validate.group(0))
        sum += (int(mlist[0])*int(mlist[1]))
print(sum)
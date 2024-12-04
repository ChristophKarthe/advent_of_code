import re

textfile = open('advent_of_code/input_3.txt','r')
list = textfile.read().split("do")
statepattern = r"[n]['][t]"
pattern = r"[u][l][(]\d+[,]\d+[)]"
pattern2 = r"\d+"
sum = 0
state = 1
for i in range(0,len(list)):
    state = 1
    if re.match(statepattern, list[i]):
        state = 0
    validate = re.findall(pattern, list[i])
    for item in validate:
        mlist = re.findall(pattern2, item)
        sum += (int(mlist[0])*int(mlist[1])*state)
print(sum)
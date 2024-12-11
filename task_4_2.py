import re

textfile = open('advent_of_code/input_4.txt','r')
sum = 0
def xmascount(string):
    founditems = re.findall("XMAS", string)
    founditems2 = re.findall("SAMX", string)
    return (len(founditems) + len(founditems2))
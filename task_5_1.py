textfile = open('./input_5_example.txt','r')
array1 = textfile.read().split("\n")
array2 = []
k = -1
for i in range(-1,-len(array1),-1):
    print(len(array1[k]))
    print(k)
    print(array1)
    if len(array1[k]) >= 5:
        array2.append(array1[k])
        array1.pop(k)
        k += 1
    k -= 1
        

# for elements in array1:
#     elements.split("|")
# for elements in array2:
#     elements.split(",")

print(array1,array2)
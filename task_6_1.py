import re

textfile = open('./input_6.txt','r')
oldlocationmap = textfile.read().split("\n")
locationmap = []
for elements in oldlocationmap:
    locationmap.append(list(elements))

def findguardindexes(locationmap):
    for i in range(0, len(locationmap)):
        listguard = re.findall(r"\^|v|<|>", "".join(locationmap[i]))
        if len(listguard) != 0:
            guardindex = locationmap[i].index(listguard[0])
            return guardindex, i
        else:
            continue

def turn90degrees(guard):
    if guard == "^":
        guard = ">"
    elif guard == ">":
        guard = "v"
    elif guard == "v":
        guard = "<"
    elif guard == "<":
        guard = "^"
    return guard

def checkbounds(locationmap, guard, index1, index2):
    if index1 == 0 and guard == "^":
        return True
    elif index2 == 0 and guard == "<":
        return True
    elif index2 == len(locationmap[index1])-1 and guard == ">":
        return True
    elif index1 == len(locationmap)-1 and guard == "v":
        return True
    else:
        return False

def zaehlalgorithmus(locationmap):
    xsum = 0
    for element in locationmap:
        countx = re.findall(r"X","".join(element))
        xsum = xsum + len(countx)
    return xsum +1
    
while not checkbounds(locationmap, locationmap[findguardindexes(locationmap)[1]][findguardindexes(locationmap)[0]], findguardindexes(locationmap)[1], findguardindexes(locationmap)[0]):
    guardindexes = findguardindexes(locationmap)
    guard = locationmap[guardindexes[1]][guardindexes[0]]
    forwardindexes = [0,0]
    if guard == "^":
        forwardindexes[0] = guardindexes[1] - 1
        forwardindexes[1] = guardindexes[0]
    elif guard == ">":
        forwardindexes[0] = guardindexes[1]
        forwardindexes[1] = guardindexes[0] + 1
    elif guard == "v":
        forwardindexes[0] = guardindexes[1] + 1
        forwardindexes[1] = guardindexes[0]
    elif guard == "<":
        forwardindexes[0] = guardindexes[1]
        forwardindexes[1] = guardindexes[0] - 1
    
    if locationmap[forwardindexes[0]][forwardindexes[1]] == "#":
        locationmap[guardindexes[1]][guardindexes[0]] = turn90degrees(guard)
        continue
    else:
        locationmap[forwardindexes[0]][forwardindexes[1]] = guard
        locationmap[guardindexes[1]][guardindexes[0]] = "X"

# for elements in locationmap:
#     print("".join(elements))

print(zaehlalgorithmus(locationmap))
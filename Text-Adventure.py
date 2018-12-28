"Text Adventure"

import os

no_rooms = len(os.listdir("./rooms"))
list_rooms = [[] for i in range(no_rooms)]

i = -1
for room in os.listdir("./rooms"):
    i += 1
    print(room)
    os.chdir("./rooms")
    dictionary = {}
    file = open(room)
    for line in file:
        print(line)
        dictionary[line.split(": ")[0]] = line.split(": ")[1]
        print(line.split(": "))
    list_rooms[i] = dictionary
    file.close()
    os.chdir("..")

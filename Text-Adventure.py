"Text Adventure"

"""
Import required modules. 
"""
import os

"""
Read the number of room_x.txt files in the rooms directory and make a list of 
empty lists of this length.
"""
no_rooms = len(os.listdir("./rooms"))
list_rooms = [[] for i in range(no_rooms)]

"""
For each room_x.txt file in the rooms directory, write its contents to a 
dictionary and add each dictionary to list_rooms.
"""
i = -1
for room in os.listdir("./rooms"):
    i += 1
    os.chdir("./rooms")
    list_rooms[i] = {}
    file = open(room)
    for line in file:
        list_rooms[i][line.split(": ")[0]] \
        = \
        str.strip(line.split(": ")[1])
    file.close()
    os.chdir("..")


"Text Adventure"

# Import required modules.
import os

# Read the number of room_x.txt files in the rooms directory and make a list
# of empty lists of this length.
no_rooms = len(os.listdir("./rooms"))
list_rooms = [[] for i in range(no_rooms)]
player_start = 0

# For each room_x.txt file in the rooms directory, write its contents to a
# dictionary and add each dictionary to list_rooms.
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


# Write the contents of commands.txt to a commands dictionary
commands = {}
file = open("commands.txt")
for line in file:
    commands[line.split(": ")[0]] \
        = \
        eval(str.strip(line.split(": ")[1]))
file.close()

# Write the contents of commands_text.txt to a commands_text dictionary
commands_text = {}
file = open("commands_text.txt")
for line in file:
    commands_text[line.split(": ")[0]] \
        = \
        str(str.strip(line.split(": ")[1]))
file.close()


print("""For a list of available commands, type "help".\n""")
print(list_rooms[player_start]["description_first"])
running = True
while running is not False:
    player_input = str(input())
    for i in commands["help"]:
        if player_input == i:
            print(commands_text["help"])
    for i in commands["quit"]:
        if player_input == i:
            running = False

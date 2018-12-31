"Text Adventure"

# Import required modules.
import os

# Read the number of "room_x.txt" files in the rooms directory and make a
# "list_rooms" list of empty lists of this length.
no_rooms = len(os.listdir("./rooms"))
list_rooms = [[] for i in range(no_rooms)]
player_start = 4
current_room = player_start

# For each "room_x.txt" file in the rooms directory, write its contents to a
# dictionary and add each dictionary to "list_rooms".
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


# Write the contents of "commands.txt" to a "commands" dictionary
commands = {}
file = open("commands.txt")
for line in file:
    commands[line.split(": ")[0]] \
        = \
        eval(str.strip(line.split(": ")[1]))
file.close()

# Write the contents of "commands_text.txt" to a "commands_text" dictionary
commands_text = {}
file = open("commands_text.txt")
for line in file:
    commands_text[line.split(": ")[0]] \
        = \
        str(str.strip(line.split(": ")[1]))
file.close()


# Define a "room_change" function which changes the player's current room based
# on their input, provided there is a door leading from their current room to
# their desired room.
def room_change(direction):
    global current_room
    for i in commands[str("go_" + direction)]:
        if player_input == i:
            if list_rooms[current_room][str("door_" + direction)] == str(True):
                print("\nYou go through the door.")
                current_room = int(list_rooms[current_room][str("connect_" +
                                   direction)])
                if list_rooms[current_room]["visited"] == str(False):
                    print("\n" + list_rooms[current_room]["description_first"])
                elif list_rooms[current_room]["visited"] == str(True):
                    print("\n" +
                          list_rooms[current_room]["description_visited"])
                list_rooms[current_room]["visited"] = str(True)
            else:
                print("This door doesn't exist")
    return()


# Print initial text, set up "help" and "quit" commands and call the
# "room_change" function for each direction.
print("""For a list of available commands, type "help".\n""")
print(list_rooms[player_start]["description_first"])
list_rooms[player_start]["visited"] = str(True)
running = True
while running is not False:
    player_input = str(input())
    for i in commands["help"]:
        if player_input == i:
            print(commands_text["help"])
    for i in commands["quit"]:
        if player_input == i:
            running = False
    room_change("n")
    room_change("e")
    room_change("s")
    room_change("w")

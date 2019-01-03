" --- Text Adventure --- "


# Import required modules.
import os

# Define initial conditions.
player_start = 0
current_room = player_start


"""
--- The following section handles reading and storing data from text files  ---
"""


# Define a "read_files" function to read the contents of the files in a
# specified "name" directory to a list of dictionaries, and return this list
# along with the number of files in the directory.
def read_files(name):
    number = len(os.listdir("./" + str(name) + "s"))
    list = [[] for i in range(number)]
    i = -1
    for object in os.listdir("./" + str(name) + "s"):
        i += 1
        os.chdir("./" + str(name) + "s")
        list[i] = {}
        file = open(object)
        for line in file:
            list[i][line.split(": ")[0]] \
                = \
                eval(str.strip(line.split(": ")[1]))
        file.close()
        os.chdir("..")
    return(number, list)


# Define a "read_files_home" function to read the contents of a specified
# "name" file in the main working directory to a dictionary and return this
# dictionary.
def read_files_home(name):
    dictionary = {}
    file = open(str(name) + ".txt")
    for line in file:
        dictionary[line.split(": ")[0]] \
            = \
            eval(str.strip(line.split(": ")[1]))
    file.close()
    return(dictionary)


# Call the "read_files" function to read the contents of the room and object
# files in their respective directories to lists of dictionaries.
no_rooms, list_rooms = read_files("room")
no_objects, list_objects = read_files("object")

# Call the "read_files_home" function to read the contents of the commands.txt
# and commands_text.txt files to dictionaries.
commands = read_files_home("commands")
commands_text = read_files_home("commands_text")


"""
--- The following section handles player input and game output. ---
"""


# Define a "room_change" function which changes the player's current room based
# on their input, provided there is a door leading from their current room to
# their desired room.
def room_change(direction):
    global current_room
    for i in commands[str("go_" + direction)]:
        if player_input == i:
            if list_rooms[current_room][str("connect_" + direction)] \
                    is not False:
                print("\nYou go through the door.")
                current_room = list_rooms[current_room][str("connect_" +
                                                            direction)]
                if list_rooms[current_room]["visited"] is False:
                    print("\n" + list_rooms[current_room]["description_first"]
                          + "\n")
                elif list_rooms[current_room]["visited"] is True:
                    print("\n" +
                          list_rooms[current_room]["description_visited"] +
                          "\n")
                list_rooms[current_room]["visited"] = True
            else:
                print("This door doesn't exist")
        else:
            pass
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
            print(commands_text["quit"])
            running = False
    room_change("n")
    room_change("e")
    room_change("s")
    room_change("w")
    for i in commands["look"]:
        for j in range(no_objects):
            for k in list_objects[j]["input_names"]:
                if player_input == str(i + k):
                    if list_objects[j]["room_location"] == current_room:
                        print("\n" + list_objects[j]["description"])

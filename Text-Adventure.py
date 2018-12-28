"Text Adventure"

file = open("room_1.txt")
room_1 = {}
for line in file:
    room_1[line.split(": ")[0]] = line.split(": ")[1]
file.close()
    
#    d['mynewkey'] = 'mynewvalue'

#file = open("room_1.txt")    
#for i, line in enumerate(file, 1):
#    if i % 2 == 0:
#        print(i)
#        print(line)


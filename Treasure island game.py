print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("You arrive at a mysterious island with a map leading to hidden treasure.")
print("But danger lies in every path you take…")

print("You land on a Sandy beach. Ahead you see:")
print("1. A Dark Jungle Path:")
print("2. A rocky Cave:")
print("3. A wooden boat tied to a palm tree:")

select_path = input("Select your path: 1 or 2 or 3: ")
if select_path == "1":
    print("Ah, you chose the Jungle path, as you go inside the jungle you hear a strange noises,")
    print("you chase the noise and find a Parrot")
    jungle_choices = input("you have 2 choices: 1. follow the parrot or 2. ignore it and keep walking in search ofd the treasure: ")
    if jungle_choices == "1":
        print("The parrot guides you to the treasure, Hooray!!!")
    elif jungle_choices == "2":
        print("you kept walking inside the jungle, now you are lost forever in the jungle.:(")
    else:
        print("please select the correct choice...")

if select_path == "2":
    print("Ah, you chose the Rocky cave path")
    print("the cave is dark, scary and full of creepy noises")
    cave_choices = input("1. Light up a torch or 2. keep walking in the dark: ")
    if cave_choices == "1":
        print("You scare away the bats with the torch and found some silver coins, pretty cool !!!")
    elif cave_choices == "2":
        print("you kept walking in the dark and fell in the pit, game over")

if select_path == "3":
    print("Ah, you chose the Wooden boat path")
    print("the boats drifts into the sea")
    boat_choices = input("1. you get on and row the boat towards a shiny object or 2. row the boat to the shore: ")
    if boat_choices =="1":
        print("damn, it's a pirate trap, you are captured by pirates🏴‍☠️")
    elif boat_choices == "2":
        print("you found a map under the boat seat and followed it and found the cave treasure, YAY !!!")
    else:
        print("Choose the correct options")
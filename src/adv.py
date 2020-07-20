from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("axe", "it does what you think it does")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
name = input("what is your name, adventurer?\n")

print(f"Welcome {name}. You're a brave adventurer!\n")
print(f"""in order play this game you'll need to select the direction you wish to move.\n
You're choices include North(n), South(s), East(e), West(w), or quit(q)""")

# Make a new player object that is currently in the 'outside' room.
player = Player({name}, room['outside'], [])
print(f"your currently in {player.current_room} room\n")
print(room['outside'].description)


direction = ("n", "s", "w", "e", "q", "g", "d")
# Write a loop that:
response = ""
while response not in direction:

    response = input("What direction would you like to go? ")

    print("----------------------------")
    #print(f"You're currently holding {player.inventory}")
    print("----------------------------")

    if response == "n":
        if player.current_room == room['outside'] or room['narrow'] or room['foyer']:
            player.move(response)
            response = ""
            print("----------------------------")
        else:
            print("That's not where adventure calls")
            response = ""

    elif response == "s":
        player.move(response)
        response = ""
        print("----------------------------")

    elif response == "e":
        player.move(response)
        response = ""
        print("----------------------------")

    elif response == "w":
        player.move(response)
        response = ""
        print("----------------------------")

    elif response == "g":
        if player.current_room.get_item != []:
            player.get_item()
            print([item.name for item in player.inventory])
            response = ""

        else:
            print("There's nothing in the room")

    elif response == "i":
        print(f"Player inventory:{player.inventory}")

    elif response == "q":
        sys.exit("gg")
        break

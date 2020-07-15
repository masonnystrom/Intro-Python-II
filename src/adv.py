from room import Room
from player import Player
import sys

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
direction = ("n", "s", "w", "e")
name = input("what is your name, adventurer?\n")
print(f"Welcome {name}. You're a brave adventurer!")
print(f"""in order play this game you'll need to select the direction you wish to move.
        You're choices include North(n), South(s), East(e) or West(w)""")

# Make a new player object that is currently in the 'outside' room.
player = Player({name}, room['outside'])

# Write a loop that:
while True:
    print(f"your currently in {player.current_room} room")
    print(room['outside'].description)
    print("----------------------------")
    player_choice = (input("Would you like to go North(n), South(s), East(e), West(w)"))
    if player_choice == "n":
        player.current_room == room['foyer']
        print("onward")
    elif player_choice == "q":
        sys.exit()
    else:
        print("the cave beckons")
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

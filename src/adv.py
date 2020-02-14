from room import Room
from player import Player
from item import *
from time import sleep
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

    'lair': Room("Dragon's Lair", """You have entered the forbidden lair of the
mighty dragon! It is too dark to see and you dare not stumble blindly forward.""")
}

item = {'hook': Item("hook", "A sturdy rope with a hook on the end",
[room['overlook']], throw_hook), 'lantern': Item("lantern", """A brightly shining
lantern""", [room['lair']], light), 'claw': Item('claw', """A wicked claw of some
long-dead beast""", [all for all in room.values()], combine), 'rope': Item('rope', """A
coil of sturdy rope""", [all for all in room.values()], combine)}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make items

room['outside'].items = [item["lantern"]]
room['treasure'].items = [item["claw"]]
room['overlook'].items = [item["rope"]]
#
# Main
#
directions = ('n', 'e', 's', 'w')
play = input("Choose a character name: ")
# Make a new player object that is currently in the 'outside' room.
character = Player(play, room['outside'], [])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print("-------------------------------------------------------------------")
    print(character.location)
    action = input("What would you like to do?")
    print("-------------------------------------------------------------------")
    if action in directions:
        character.move(action)
    elif action == "q":
        print("Thanks for playing!")
        sys.exit()
    elif "get " in action:
        itemget = action.replace('get ', "")
        if itemget in [item.name for item in character.location.items]:
            character.location.items.remove(item[itemget])
            character.inventory.append(item[itemget])
            print(f'You get the {itemget}')
        else:
            print("You can't get ye flask")
    elif "drop " in action:
        itemdrop = action.replace('drop ', "")
        if itemdrop in character.inventory:
            character.inventory.remove(itemdrop)
            character.location.items.append(itemdrop)
        else:
            print("You need to have something to drop it")
    elif action in ["status", "inventory"]:
        print(character)
    elif "use " in action:
        itemuse = action.replace('use ', '')
        if itemuse in [item.name for item in character.inventory]:
            if character.location in item[itemuse].use_case:
                item[itemuse].effect(room, item, character)
                sleep(1)
            else:
                print("You can't use that here")
        else:
            print("You don't have anything like that.")
    elif action == "devtest":
        print([all for all in room])
    else:
        print("""move around with n, e, s, or w, pick up, use, or drop items,
or quit with q""")

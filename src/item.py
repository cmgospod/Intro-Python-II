class Item():
    def __init__(self, name, description, use_case, effect):
        self.name = name
        self.description = description
        self.use_case = use_case
        self.effect = effect

    def __str__(self):
        return self.name

def throw_hook(room, item, character):
    print("""You wind up and throw your grappling hook across the chasm,
and it latches securely on a large rock.""")
    room['overlook'].n_to = room['lair']
    room['lair'].s_to = room['overlook']
    room['overlook'].description = """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance. Your grappling hook offers the only way across."""
    character.inventory.remove(item['hook'])

def light(room, item, character):
    print("""You raise your lantern for a better look. The lair is just as
empty as the treasure chamber before it.""")
    room['lair'].description = """You have entered the forbidden lair of
the mighty dragon! Thankfully it does not appear to be in right now"""

def combine(room, item, character):
    if item['claw'] in character.inventory and item['rope'] in character.inventory:
        character.inventory.remove(item['claw'])
        character.inventory.remove(item['rope'])
        character.inventory.append(item['hook'])
        print("You combine the claw and the rope into a makeshift grappling hook")
    else:
        print("You don't have anything to use this with")

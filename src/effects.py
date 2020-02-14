def throw_hook(room):
    print("""You wind up and throw your grappling hook across the chasm, and it
latches securely on a large rock.""")
    room['overlook'].n_to = room['lair']
    room['lair'].s_to = room['overlook']
    room['overlook'].description = """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance. Your grappling hook offers the only way across."""

def light(room):
    print("""You raise your lantern for a better look. The lair is just as
empty as the treasure chamber before it.""")
    room['lair'].description = """You have entered the forbidden lair of
the mighty dragon! Thankfully it does not appear to be in right now"""

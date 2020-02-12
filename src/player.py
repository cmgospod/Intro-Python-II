# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    """
    Contains information about the player.
    """
    def __init__(self, playername, location, points):
        self.playername = playername
        self.location = location
        self.points = points

    def __str__(self):
        return self.playername + ": " + self.points

    def move(self, direction):
        if getattr(self.location, f'{direction}_to'):
            self.location = getattr(self.location, f'{direction}_to')
        else:
            print("You can't go there")

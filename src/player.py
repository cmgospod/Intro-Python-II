# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    """
    Contains information about the player.
    """
    def __init__(self, playername, location, inventory=[]):
        self.playername = playername
        self.location = location
        self.inventory = inventory
    def __str__(self):
        shortchar = f'{self.playername} is in the {self.location.name}.'
        if self.inventory:
            return shortchar + " carrying " + str([item.name for item in self.inventory]).replace("'", "")
        else:
            return shortchar
    def move(self, direction):
        if getattr(self.location, f'{direction}_to'):
            self.location = getattr(self.location, f'{direction}_to')
        else:
            print("You can't go there")

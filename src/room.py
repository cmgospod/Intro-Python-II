# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    """
    Class for individual rooms, with a string name and description. "To"
    variables point at adjacent rooms, while items should be a list.
    """
    def __init__(self, name, description, n_to=None, s_to=None,
                 e_to=None, w_to=None, items=[], usable=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
        self.usable = usable
    def __str__(self):
        shortroom = self.name + ": " + self.description
        if self.items:
            return shortroom + "\nitems:" + str(self.items).replace("'", "")
        else:
            return shortroom

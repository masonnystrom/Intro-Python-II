# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    """ class for room within the adventure game"""
    def __init__(self, name, description, item=None, n_to=None, s_to=None, e_to=None, w_to=None,):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.item = item
    def __str__(self):
        location = f"Name = {self.name}\nDescription = {self.description}"
        return location

    def get_item(self):
        return self.item

    def where_to_next(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to

        else:
            print("Adventure calls another way")
            return None
# new class with items for rooms and player

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


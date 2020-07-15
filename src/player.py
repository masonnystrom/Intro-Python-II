# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    """class for player that will move through the adventure game"""
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Name = {self.name}\n current room = {self.current_room}"
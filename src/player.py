# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player():
    """class for player that will move through the adventure game"""
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"Name = {self.name}\n current room = {self.current_room}"

    def move(self, response_direction):
        new_spot = self.current_room.where_to_next(response_direction)
        if new_spot != None:
            self.current_room = new_spot
        print(f"{self.name} has moved to {self.current_room}")

    def get_item(self):
        self.inventory.append(self.current_room.item)
        print(f"{self.name} picked up the {self.inventory} from {self.current_room}.")

    def drop_item(self, inventory):
        if inventory in self.inventory:
            self.inventory.remove(inventory)
        print(f"{self.name} dropped the {inventory} from {self.current_room}.")

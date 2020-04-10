# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(f"Now in {self.current_room.name}")
            print(f"This room is {self.current_room.desc}. \n")

        else:
            print(">>> You can not move in that direction! <<< \n")

    def __str__(self):
        return f"{self.name} is currently in {self.current_room}"
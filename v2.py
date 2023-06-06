# Add a treasure in a room that the player needs to find. Also add a monster that roams between the rooms.

import random

class Room:
    def __init__(self, description: str, monster: bool, treasure: bool):
        self.description = description
        self.monster = monster
        self.treasure = treasure
        self.connected_rooms = {}

    def add_room(self, direction: str, room):
        self.connected_rooms[direction] = room


class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms[0]
        self.monster_room = self.rooms[random.randint(1, 3)]
        self.game_over = False

    def create_rooms(self):
        room1 = Room("You're in a spooky room with three doors.", False, False)
        room2 = Room("This room is full of gold.", False, True)
        room3 = Room("This room is cold and empty.", False, False)
        room4 = Room("This room is warm and cozy.", False, False)

        room1.add_room("left", room2)
        room1.add_room("right", room3)
        room1.add_room("forward", room4)

        room2.add_room("back", room1)
        room3.add_room("back", room1)
        room4.add_room("back", room1)

        return [room1, room2, room3, room4]

    def move_monster(self):
        possible_rooms = [room for room in self.rooms if room != self.monster_room and room != self.current_room]
        self.monster_room.monster = False
        self.monster_room = random.choice(possible_rooms)
        self.monster_room.monster = True

    def play(self):
        while not self.game_over:
            print(self.current_room.description)

            if self.current_room.monster:
                print("Oh no, a monster! GAME OVER")
                self.game_over = True
                break

            if self.current_room.treasure:
                print("You found the treasure! YOU WIN")
                self.game_over = True
                break

            command = input("Which way do you want to go? ").lower()

            if command in self.current_room.connected_rooms:
                self.current_room = self.current_room.connected_rooms[command]
                self.move_monster()
            else:
                print("You can't go that way!")


if __name__ == "__main__":
    print("Welcome to 'The Labyrinth of Ghouls and Treasures'!")
    print("Your mission is to navigate through the labyrinth, find the gold, and avoid the ghoul.")
    game = Game()
    game.play()
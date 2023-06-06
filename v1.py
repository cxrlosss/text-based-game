# This game will have three rooms and a monster in one of them. Your goal is to avoid the monster.
class Room:
    def __init__(self, description: str, monster: bool):
        self.description = description
        self.monster = monster
        self.connected_rooms = {}

    def add_room(self, direction: str, room):
        self.connected_rooms[direction] = room


def game():
    room1 = Room("You're in a spooky room with three doors.", False)
    room2 = Room("This room is full of gold. There's one door leading back.", False)
    room3 = Room("A cold wind blows from the room ahead. There's one door leading back.", True)

    room1.add_room("left", room2)
    room1.add_room("right", room3)

    room2.add_room("back", room1)
    room3.add_room("back", room1)

    current_room = room1

    while True:
        print(current_room.description)

        if current_room.monster:
            print("Oh no, a monster! GAME OVER")
            break

        command = input("Which way do you want to go? ").lower()

        if command in current_room.connected_rooms:
            current_room = current_room.connected_rooms[command]
        else:
            print("You can't go that way!")


if __name__ == "__main__":
    print("Welcome to 'The Labyrinth of Ghouls and Treasures'!")
    game()
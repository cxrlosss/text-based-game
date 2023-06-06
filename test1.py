class Room:
    def __init__(self, description: str, monster: bool, number=0):
        self.description = description
        self.monster = monster
        self.connected_rooms = {}
        self.number = number

    def add_room(self, direction: str, room):
        self.connected_rooms[direction] = room

    def __str__(self) -> str:
        return str(self.number)
        

def game():
    room1=Room("A very scary looking place. It's very dark and quiet here and two doors are leading back.", False, 1)
    room2=Room("It looks like a jungle here. What is that - In the middle is a pyramid out of gold! One door is leading back.", True, 2)
    room3=Room("It is very cold in here. Just some torches on the walls. Two doors are leading out leading back.", False, 3)
    room4=Room("Luxurious interior. Everything made out of gold and rubins. Three doors are leading out.", False, 4)

    room1.add_room("left", room2)
    room1.add_room("right", room4)

    room2.add_room("back", room1)
    

    room3.add_room("right", room2)
    room3.add_room("left", room4)
    
    room4.add_room("left", room1)
    room4.add_room("right", room3)
    room4.add_room("forward", room2)

       
    map = """
        +-----------+-----------+
        |           |           |
        |   Room 1  |   Room 4  |
        |           |           |
        +-----------+-----------+
        |           |           |
        |   Room 2  |   Room 3  |  
        |           |           |      
        +-----------+-----------+
    """
    current_room = room1

    while True:
        print(current_room.description)
        if current_room.monster:
            print("Oh no, not good, a monster! GAME OVER")
            break
        
        print(map)
        command = input(f"You are in room number {current_room}. Which way do you want to go?(left, right, in room 4 forward) ").lower()
   
        if command in current_room.connected_rooms:
            current_room = current_room.connected_rooms[command]
        else:
            print("You can't go that way!")


if __name__ == "__main__":
    print("Welcome to 'The Labyrinth of Ghouls and Treasures'!")
    game()

  


        

 
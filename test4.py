#karte
#waffen
#monster, dass sich bewegt
#schatztruhe
#räume
#map change

import random

class Room:
    def __init__(self, description: str, monster: bool, treasure: bool, potion: bool, weapon: bool, number=0):
        self.description = description
        self.monster = monster
        self.treasure = treasure
        self.potion = potion
        self.weapon = weapon
        self.number = number
        self.connected_rooms = {}

    def add_room(self, direction: str, room):
        self.connected_rooms[direction] = room

    def __str__(self) -> str:
        return str(self.number)

class Game:
    
   def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = self.rooms[0]
        self.monster_room = self.rooms[random.randint(1, 3)]
        self.game_over = False
        self.health = 100
        self.treasures_found = 0

   def create_rooms(self):
     room1=Room("You're in a cold room with torches on the walls. Two doors are leading out.", False, False, False, False, 1)
     room2=Room("A very scary looking place. It's very dark and quiet here and three doors are leading back.", False, False, False, True, 2)
     room3=Room("It looks like a jungle here. What is that - In the middle is a pyramid out of gold! Two doors are leading out.",False, True, False, False, 3)
     room4=Room("It's dark and wind blows you in the face. Three doors are leading out.", False, False, False, False, 4)
     room5=Room("You almost can't see anything. Just silence. Three doors are leading out",False, False, False, False, 5)
     room6=Room("Luxurious interior. Everything made out of gold and rubins. Three doors are leading out.", False, True, False, False, 6)
     room7=Room("Everywhere is water, but in the middle is a little island. Two doors are leading out.", False, False, True, False, 7)
     room8=Room("It seems like a junkyard here. Just trash, but something sparkles there. One door is leaing back", False, True, False, True, 8)
     room9=Room("Old ruins of a castle. On door is leading back.", False, False, False, False, 9)

     room1.add_room("forward", room2)
     room1.add_room("right", room4)

     room2.add_room("back", room1)
     room2.add_room("forward", room3)
     room2.add_room("right", room5)

     room3.add_room("right", room6)
     room3.add_room("back", room2)

     room4.add_room("forward", room5)
     room4.add_room("right", room7)
     room4.add_room("back", room1)  
   
     room5.add_room("left", room2)
     room5.add_room("forward", room6)
     room5.add_room("back", room4)

     room6.add_room("right", room9)
     room6.add_room("left", room3)
     room6.add_room("back", room5)

     room7.add_room("forward", room8)
     room7.add_room("back", room4)
  
     room8.add_room("back", room7)

     room9.add_room("back", room6)

     return [room1, room2, room3, room4, room5, room6, room7, room8, room9]
     
   def move_monster(self):
        possible_rooms = [room for room in self.rooms if room != self.monster_room]
        self.monster_room.monster = False
        self.monster_room = random.choice(possible_rooms)
        self.monster_room.monster = True
 
   def play(self):
        self.current_room = self.rooms[0] 
        while not self.game_over:
            self.move_monster()
            print(self.current_room.description)

            
            print("Map:")
            for room in self.rooms:
                if room == self.current_room:
                  print("[P]", end=" ")
                elif room == self.monster_room:
                  print("[M]", end=" ")
                else:
                  print("[ ]", end=" ")
                  
                if int(str(room)) % 3 == 0:
                    print() 

            if self.current_room.monster:
                print("Oh no, not good! A monster! You lose 30 health.")
                self.health -= 30
                if self.health <= 0:
                    print("You have 0 health. GAME OVER")
                    self.game_over = True
                else:
                    print(f"You have {self.health} health left.")
                self.move_monster()

            if self.current_room.treasure:
                print("You found a treasure!")
                self.treasures_found += 1
                self.current_room.treasure = False
            if self.treasures_found == 3:
                print("You found all the treasures! YOU WIN!")
                self.game_over = True

            if self.current_room.potion:
                print("You found a healing potion! You regain 50 health.")
                self.health += 50
                self.current_room.potion = False

        
            command = input(f"You are in room number {self.current_room}. Which way do you want to go? ").lower()

            if command in self.current_room.connected_rooms:
                self.current_room = self.current_room.connected_rooms[command]
            else:
                print("You can't go that way!")

if __name__ == "__main__":
     print("Welcome to 'The Labyrinth of Ghouls and Treasures'!")
     print("Your mission is to navigate through the labyrinth, find the gold, and avoid the ghoul. A monster is following you and tries to stop you from finding the treasures. It can harm you very bad, but you can heal yourself with a heal potion.")
     game = Game()
     game.play()
   
     
    


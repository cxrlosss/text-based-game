def show_room(current_room):
    rooms = {
        1: "Küche",
        2: "Wohnzimmer",
        3: "Schlafzimmer",
        4: "Badezimmer"
    }

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

    if current_room in rooms:
        room_name = rooms[current_room]
        map = map.replace(f"Raum {current_room}", f"[{room_name}]")

    print(map)

# Beispielaufruf
show_room(2)  # Ausgabe: Karte mit Raum 2 markiert

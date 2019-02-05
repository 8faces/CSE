world_map = {
    'Forest': {
        'NAME': "Galaxy Forest",
        'DESCRIPTION': "This is the room that you are in",
        'PATHS': {
            'NORTH': "Pink_lake",
        }
    },
    'Pink_lake': {
        'NAME': "Pink lake",
        'DESCRIPTION': "There are fish in the lake",
        'PATHS': {
            'SOUTH': 'Forest',
            'WEST': 'Dwarves_town',
        }
    },
    'Dwarves_town': {
        'NAME': "Dwarves town",
        'DESCRIPTION': "there are many Dwarves around"
        'PATHS':{}
            'EAST':'Pink lake',
    }
}


directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Forest"]
playing = True


while playing:
    print(current_node['NAME'])
    print(current_noDe['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("you can't go that way")
    else:
        print("Command no recognized")



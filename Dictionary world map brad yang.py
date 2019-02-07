print("welcome to the World of Noside")
world_map = {
    'FOREST': {
        'NAME': "Galaxy Forest",
        'DESCRIPTION': "you are in Galaxy Forest",
        'PATHS': {
            'NORTH': "PINK_LAKE_PATH"
        }
    },
    'PINK_LAKE_PATH': {
        'NAME': "Pink lake",
        'DESCRIPTION': "There are fish in the lake",
        'PATHS': {
            'SOUTH': 'FOREST',
            'WEST': 'DWARVES_TOWN',
            'NORTH': 'THE_LAKE_SHORE'
        }
    },
    'DWARVES_TOWN': {
        'NAME': "Dwarves town",
        'DESCRIPTION': "there are many Dwarves around",
        'PATHS': {
            'EAST': 'PINK_LAKE_PATH',
        }
    },
    'THE_LAKE_SHORE': {
        'NAME': "Shore of pink lake ",
        'DESCRIPTION': "You feel a slight breeze and the water is touching your feet",
        'PATHS': {
            'SOUTH': 'PINK_LAKE_PATH',
            'NORTH': 'INSIDE_LAKE'
            }
    },
    'INSIDE_LAKE': {
        'NAME': "Inside lake",
        'DESCRIPTION': "You are swimming in the lake ",
        'PATHS': {
            'DOWN': 'UNDER_WATER',
            'SOUTH': 'THE_LAKE_SHORE'
        },
    'UNDER_WATER': {
        'NAME': "Under water",
        'DESCRIPTION': 'you are under water and you se fish and a shinny thing',
        'PATHS': {
            'UP': 'INSIDE_LAKE',
            'DOWN': 'SHINNY_THING'
        }

    }
    }
}


directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["FOREST"]
playing = True


while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
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



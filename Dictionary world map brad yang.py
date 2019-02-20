print("welcome to the World of Noside")
world_map = {
    'FOREST': {
        'NAME': "South Galaxy Forest",
        'DESCRIPTION': "you are in Galaxy Forest it is so colorful",
        'PATHS': {
            'NORTH': "PINK_LAKE_PATH",
            'SOUTH': 'TOWN_OF_ENDVADOR'
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
            'WEST': 'DWARVEN_CASTLE'
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
            'DOWN': 'UNDERWATER',
            'SOUTH': 'THE_LAKE_SHORE'
        }
    },
    'UNDERWATER': {
        'NAME': "Under water",
        'DESCRIPTION': 'you are under water and you see fish and a UNDER WATER TEMPLE ',
        'PATHS': {
            'UP': 'INSIDE_LAKE',
            'DOWN': 'UNDERWATER_TEMPLE'
        }
    },
    'UNDERWATER_TEMPLE': {
        'NAME': "Under water temple",
        'DESCRIPTION': 'You found a room with air in it still',
        'PATHS': {
            'UP': 'UNDERWATER'
        }
    },
    'DWARVEN_CASTLE': {
        'NAME': "King Otar's Castle",
        'DESCRIPTION': 'This is KIng Otars castle the King of dwarves',
        'PATHS': {
            'EAST': 'DWARVES_TOWN',
        }
    },
    'TOWN_OF_ENDVADOR': {
        'NAME': "Endvador",
        'DESCRIPTION': 'You are in the town ruled by the kingdom of Beelzebub ',
        'PATHS': {
            'NORTH': 'FOREST',
            'EAST': 'ENDVADOR_MARKET',
            'WEST': ''
        }
    },
    'ENDVADOR_MARKET': {
        'NAME': "Endvador Market",
        'DESCRIPTION': 'This is the market of envador you can buy many items',
        'PATHS':{
            'WEST': 'TOWN_OF_ENDVADOR'
        }
    },
    'GLACIAL_CAVE': {
        'NAME': "Glacial Cave",
        'DESCRIPTION': 'This is the glacial cave itis a source for people of Endvador no one dares go north or west',
        'PATH': {
            'EAST': 'TOWN_OF_ENDVADOR',
            'WEST': 'DARK_REALM'
        }
    },
    'DARK_REALM': {
        'NAME': "The Dark Realm",
        'DESCRIPTION': 'Your in the dark realm you are where no man dare to seek',
        'PATH': {
            'EAST': 'GLACIAL_CAVE',
            'NORTH': 'FALLEN_KING_RUNES'
        }
    },
    'FALLEN_KING_RUNES': {
        'NAME' "Fallen king runes",
        'DESCRIPTION' 'You are at the runes of the fallen king you may find some of his treasures'
        
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



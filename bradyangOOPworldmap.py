class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, up=None, down=None,
                 person='dryads'):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.character = person


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method take a direction, and finds the variable of the
        room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exist, None if it does not
        """
        return getattr(self.current_location, direction)


forest = Room("South Galaxy Forest", "you are in Galaxy Forest it is so colorful", None,)
town_of_endvador = Room("The Town Endvador", 'You are in the town ruled by the kingdom of Beelzebub ', None, forest)
endvador_market = Room("Endvador Market", 'This is the market of envador you can buy many items', None,
                       town_of_endvador)
pink_lake = Room("The Pink Lake", "There are fish in the lake", None, forest,)
pink_lake_shore = ("Shore of pink lake ",  "You feel a slight breeze and the water is touching your feet", None
                   , pink_lake,)
inside_lake = Room("Inside lake", "You are swimming in the lake ", pink_lake, None, pink_lake_shore)
underwater = Room("Under water", 'you are under water and you see fish and a UNDER WATER TEMPLE ', None, inside_lake,)
underwater_Temple = Room("Under water temple", 'You found a room with air in it still', None, )
dwarves_town = Room("Dwarves Town", None,  "there are many Dwarves around", None, pink_lake)
dwarven_castle = Room("King Otar's Castle", "This is KIng Otars castle the King of dwarves", None, dwarves_town, )
ice_cave = Room("Glacial Cave", "You look around and see nothing but ice it is cold", None, town_of_endvador)
frost_forest = Room("Frost Forest", "You see snow everywhere and it's very cold.", None, ice_cave)
dark_realm = Room("The Dark Realm", 'Your in the dark realm you are where no man dare to seek', None, ice_cave)
fall_kingdom = Room("Fallen kingdom runes", 'You are at the runes of the fallen king you may find some of his treasures'
                    , None, dark_realm,)
game_room = Room("The Game Dimension", "There are lots of games here", None, frost_forest)
time_room = Room("Time Dimension", 'You are in the time dimension', None, frost_forest)

forest.south = town_of_endvador
forest.north = pink_lake
pink_lake.south = forest
pink_lake.west = dwarves_town
pink_lake.north = pink_lake_shore
pink_lake_shore.south = pink_lake
pink_lake_shore.north = inside_lake
inside_lake.down = underwater
inside_lake.south = pink_lake_shore
inside_lake.south = pink_lake_shore
underwater.up = inside_lake
underwater.down = underwater_Temple
underwater_Temple.up = underwater
dwarves_town.east = pink_lake
dwarves_town.west = dwarven_castle
dwarven_castle.east = dwarves_town
town_of_endvador.north = forest
town_of_endvador.west = ice_cave
town_of_endvador.east = endvador_market
ice_cave.east = town_of_endvador
ice_cave.north = frost_forest
ice_cave.west = dark_realm
dark_realm.north = fall_kingdom
dark_realm.east = ice_cave
fall_kingdom.south = dark_realm
frost_forest.south = ice_cave
frost_forest.down = game_room
frost_forest.north = time_room
game_room.up = frost_forest
time_room.south = frost_forest


# OPTION 2 -use strings, but more difficult controller
# R19A = Room("MR. Wiebe's Room",)
# parking_lot = Room("The Parking Lot", None, "R19A")

player = Player(forest)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True


while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("you can't go that way")
    else:
        print("Command no recognized")
# class Boss(object):


# These are the instances of the rooms (instantiation
# R19A = Room("MR. Wiebe's Room", )
# parking_lot = Room("The Parking Lot", None, R19A)
# OPTION 1 - use variable, but fix later

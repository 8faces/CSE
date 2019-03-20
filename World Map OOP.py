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


Dark_realm = Room("Dark Realm", "Your in the dark realm you are where no man dare to seek", None,)
Town_of_Envador = Room("Town of Endvador", 'This is the market of envador you can buy many items', None)

Forest = Room("South Galaxy Forest", "you are in Galaxy Forest it is so colorful", None, Town_of_Envador,)
Underwater_Temple = Room( "Under water temple", 'You found a room with air in it still', None)


pink_lake = Room("The Pink Lake", None, Forest,)

Dwarves_town = Room("Dwarves Town", None, pink_lake,)
Dwarven_castle = Room("King Otar's Castle", "This is KIng Otars castle the King of dwarves", None, Dwarves_town, )

Forest.south = Town_of_Envador
Forest.north = pink_lake
pink_lake.west = Dwarves_town
Dwarves_town.west = Dwarven_castle

# OPTION 2 -use strings, but more difficult controller
# R19A = Room("MR. Wiebe's Room",)
# parking_lot = Room("The Parking Lot", None, "R19A")

player = Player(Forest)

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

class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None,):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west


# These are the instances of the rooms (instantiation
# R19A = Room("MR. Wiebe's Room", )
# parking_lot = Room("The Parking Lot", None, R19A)
# OPTION 1 - use variable, but fix later
Forest = Room("South Galaxy Forest", None, Town_of_Envador,)
pink_lake = Room("The Pink Lake", None, Forest)
Dwarves_town = Room("Dwarves Town", None, pink_lake)
Town_of_Envador = Room("Town of Endvador", None, )



Forest.south = pink_lake
pink_lake.west = Dwarves_town

# OPTION 2 -use strings, but more difficult controller
R19A = Room("MR. Wiebe's Room", )
parking_lot = Room("The Parking Lot", None, "R19A")


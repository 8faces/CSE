class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None,):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west


# These are the instances of the rooms (instantiation

# OPTION 1 - use variable, but fix later
R19A = Room("MR. Wiebe's Room", )
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# OPTION 2 -use strings, but more difficult controller
R19A = Room("MR. Wiebe's Room", )
parking_lot = Room("The Parking Lot", None, "R19A")

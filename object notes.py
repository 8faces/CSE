class Laptop(object) :
    def __init__(self, screen_resolution, extra_space, colour):
        # Thing that laptops has
        # Everything in this list should be relevant to the program
        self.processor = "intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"

    def charge(self, time):    
        # Computer is already charged
        if self.battery_left >= 100:
            print("The computer is already charge")
            return

        self.battery_left += time  # This adds to the battery life
        # Computer is mostly charged
        if self.battery_left > 100:
            print("The computer quickly charges")
            self.battery_left = 100
        # Computer is not charged at all
        else:
            print("The computer is now at $d%% " % self.battery_left)


my_computer = Laptop("1920x1080", 10000, "Rainbow")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("10000000000000000000000000000x1111111111111111111111111111111", 5555555555555555555555555, "1")











class Laptop(object):
    def __init__(self, screen_resolution, extra_space=1000, colour="Cobalt"):
        # Thing that laptops has
        # Everything in this list should be relevant to the program
        self.processor = "intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
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
                print("The computer is now at %d%% " % self.battery_left)
        else:
            print("It's broken. Good job")

    def smash(self):
        self.functioning = False
        print("I took the laptop....")
        print()
        print()
        print()
        print("...AND I THREW IT ON THE GROUND!!!!!")

    def use(self, time):
        self.battery_left -= time
        print("You use the laptop for %s minutes" % time)


my_computer = Laptop("1920x1080", 10000, "Rainbow")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("10000000000000000000000000000x1111111111111111111111111111111", 5555555555555555555555555, "1")
default_computer = Laptop("1920x1080")

my_computer.use(60)
my_computer.charge(20)
my_computer.charge(1000)
my_computer.smash()
my_computer.charge(20)

your_computer.charge(20)







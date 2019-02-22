class Shield(object):
    def __init__(self, grip):

        self.durability = 100
        self.grip = grip
        self.protection = 100
        self.emblem = "water_emblem"
        self.equipped = True
        self.mana = 100

    def harden(self):
        self.durability += 150
        print("Now you have power!!!!!")
        return

    def block(self):
        self.protection += 100
        self.mana -= 20
        print("You have magic shield around you!!")

    def bash(self):
        self.mana -= 60
        print("You hit nothing you just wasted mana?")


my_shield = Shield(True)
my_shield.harden()
my_shield.block()
my_shield.bash()


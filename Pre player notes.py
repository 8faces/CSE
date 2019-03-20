class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.helm_slot = None
        self.chest_slot = None
        self.weapon_slot = None
        self.item_slot = None
        self.health = health
        self.weapon = weapon
        self.armor = armor


sword = weapon
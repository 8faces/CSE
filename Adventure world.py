class Item(object):
    def __init__(self, name):
        self.name = name
        self.equipped = False


class Weapon(Item):
    def __init__(self, name, damage, sharpness, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.sharpness = sharpness
        self.durability = durability

    def attack(self):
        self.equipped = True
        self.sharpness -= 100
        print("Nicu hit")

    def block(self):
        self.durability -= 10
        self.sharpness -= .5
        print("Wow what a great block")

    def parry(self):
        self.durability -= 50
        self.sharpness -= 4
        print("Look at the moves Faker")


class Sword1(Weapon):
    def __init__(self, name, damage, sharpness, durability):
        super(Sword1, self).__init__(name, damage, sharpness, durability)


class Spear(Weapon):
    def __init__(self, name, damage, sharpness, durability):
        super(Spear, self).__init__(name, damage, sharpness, durability)


class Defense(Item):
    def __init__(self, name, armor, hitponits):
        super(Defense, self).__init__(name)
        self.armor = armor
        self.hitponits = hitponits


class Shield(Defense):
    def __init__(self, name, armor, hitponits):
        super(Shield, self).__init__(name, armor, hitponits)
        self.armor = 500
        self.hitponits = 1500


class Consumable(Item):
    def __init__(self, name, consume):
        super(Consumable, self).__init__(name)
        self.consume = consume


class WearableArmor(Item):
    def __init__(self, name, armor_amt, durability):
        super(WearableArmor, self).__init__(name)
        self.armor_amt = armor_amt
        self.durability = durability


class Helmet(WearableArmor):
    def __init__(self, name,  armor_amt, durability):
        super(Helmet, self).__init__(name, armor_amt, durability)


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

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("no Damage is done because your awe so me")
        self.health -= damage - self.armor.armor_amt
        if self.health < 0:
            self.health = 0
            print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, up=None, down=None,
                 person=person):
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

class Item(object):
   def __init__(self, name):
       self.name = name


class Weapon(Item):
   def __init__(self, name, damage, sharpness, durability):
       super(Weapon, self).__init__(name)
       self.damage = damage
       self.sharpness = sharpness
       self.durability = durability

   def attack(self):

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


class Sword(Weapon):
   def __init__(self, name, damage, sharpness, durability):
       super(Sword, self).__init__(name, damage, sharpness, durability)


class Staff(Weapon):
   def __init__(self, name, damage, sharpness, durability):
       super(Staff, self).__init__(name, damage, sharpness, durability)


class Spear(Weapon):
   def __init__(self, name, damage, sharpness, durability):
       super(Spear, self).__init__(name, damage, sharpness, durability)


class Grimoire(Item):
   def __init__(self, name):
       super(Grimoire, self).__init__(name)


class Coin(Item):
   def __init__(self, name):
       super(Coin, self).__init__(name)


class Goldcoin(Coin):
   def __init__(self, name):
       super(Goldcoin, self).__init__(name)


class Silvercoin(Coin):
   def __init__(self, name):
       super(Silvercoin, self).__init__(name)


class Bronzecoin(Coin):
   def __init__(self, name):
       super(Bronzecoin, self).__init__(name)


class Defense(Item):
   def __init__(self, name, armor, hitpoints):
       super(Defense, self).__init__(name)
       self.armor = armor
       self.hitpoints = hitpoints


class Shield(Defense):
   def __init__(self, name, armor, hitpoints):
       super(Shield, self).__init__(name, armor, hitpoints)
       self.armor = 500
       self.hitpoints = 1500


class WearableArmor(Item):
   def __init__(self, name, armor_amt, durability):
       super(WearableArmor, self).__init__(name)
       self.armor_amt = armor_amt
       self.durability = durability


class BodyPillow(WearableArmor):
   def __init__(self, name, armor_amt, durability):
       super(BodyPillow, self).__init__(name, armor_amt, durability)


class Helmet(WearableArmor):
   def __init__(self, name, armor_amt, durability):
       super(Helmet, self).__init__(name, armor_amt, durability)


class ChestPlate(WearableArmor):
   def __init__(self, name, armor_amt, durability):
       super(ChestPlate, self).__init__(name, armor_amt, durability)


class Leggings(WearableArmor):
   def __init__(self, name, armor_amt, durability):
       super(Leggings, self).__init__(name, armor_amt, durability)


class Boots(WearableArmor):
   def __init__(self, name, armor_amt, durability):
       super(Boots, self).__init__(name, armor_amt, durability)


class Consumable(Item):
   def __init__(self, name):
       super(Consumable, self).__init__(name)
       self.consume = True


class Elixir(Consumable):
   def __init__(self, name, ):
       super(Elixir, self).__init__(name)


class InstantNoodles(Consumable):
   def __init__(self, name, ):
       super(InstantNoodles, self).__init__(name)


class Ring(Item):
   def __init__(self, name):
       super(Ring, self).__init__(name)


class ElementStones(Item):
   def __init__(self, name):
       super(ElementStones, self).__init__(name)
       self.power = False


class FireStone(ElementStones):
   def __init__(self, name):
       super(FireStone, self).__init__(name)

   def burn(self):
       self.power = True


class IceStone(ElementStones):
   def __init__(self, name):
       super(IceStone, self).__init__(name)

   def freeze(self):
       self.power = True


class WindStone(ElementStones):
   def __init__(self, name):
       super(WindStone, self).__init__(name)

   def tornado(self):
       self.power = True


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
                person=None, items=None):

       if items is None:
           items = []
       self.name = name
       self.north = north
       self.south = south
       self.east = east
       self.west = west
       self.up = up
       self.down = down
       self.description = description
       self.character = person
       self.items = items


Noodles = InstantNoodles("Instant noodles")
Dragon_Shield = Shield("Dragon Shield", armor=400, hitpoints=600)
Wood_Shield = Shield("wood shield", armor=100, hitpoints=150)
Iron_Shield = Shield("Iron shield", armor=200, hitpoints=300)
Wood_Sword = Sword("Wood Sword", sharpness=10, damage=30, durability=100)
Iron_Sword = Sword("Iron sword", sharpness=50, damage=80, durability=300)
Iron_spear = Spear("Iron spear", sharpness=40, damage=70, durability=300)
Longinus_Smasher = Spear("Longinus Smasher ", sharpness=2000000, damage=5000, durability=1500000)
Iron_helmet = Helmet("Iron Helmet", armor_amt=150, durability=200)
Wood_helmet = Helmet("Wood Helmet", armor_amt=80, durability=100)
wifu1 = BodyPillow("Zero Two", armor_amt=100000, durability=1000000)
wifu2 = BodyPillow("Takagasi", armor_amt=100000, durability=1000000)
wifu3 = BodyPillow("Asuna", armor_amt=100000, durability=1000000)
Gcoin = Coin("Gold Coin")
Scoin = Coin("Silver Coin")
Bcoin = Coin("Bronze Coin")


forest = Room("South Galaxy Forest", "you are in Galaxy Forest it is so colorful", None, None, None, None, None, None,
             None, [Noodles, Wood_helmet, Wood_Sword, Wood_Shield])
town_of_endvador = Room("The Town Endvador", 'You are in the town ruled by the kingdom of Beelzebub ', forest, None,
                       None, None, None, None, None, )
endvador_market = Room("Endvador Market", 'This is the market of envador you can buy many items', None, None, None,
                      town_of_endvador, None, None, None, [Iron_helmet, Iron_Sword, ])
pink_lake = Room("The Pink Lake Path", "There are fish in the lake", None, forest, None, None, None, None, None, )
pink_lake_shore = Room("Shore of pink lake ",  "You feel a slight breeze and the water is touching your feet", None,
                      pink_lake, [Bcoin, Scoin])
inside_lake = Room("Inside lake", "You are swimming in the lake ", None, None, None, None, None, None, None, pink_lake,)
underwater = Room("Under water", 'you are under water and you see fish and a UNDER WATER TEMPLE ', None, None, None,
                 None, None, None, None, inside_lake,)
underwater_Temple = Room("Under water temple", 'you are in the final boss room!!!you willl die!!!', None, None, None,
                        None, None, None, None,)
dwarves_town = Room("Dwarves Town", "there are many Dwarves around", None, None, None, None, None, None, None,
                   pink_lake)
dwarven_castle = Room("King Otar's Castle", "This is KIng Otars castle the King of dwarves", None, None, None, None,
                     None, None, dwarves_town, [Iron_Shield, ])
ice_cave = Room("Glacial Cave", "You look around and see nothing but ice it is cold", None, None, None, None, None,
               None, town_of_endvador, [Gcoin, Iron_spear])
frost_forest = Room("Frost Forest", "You see snow everywhere and it's very cold.", None, None, None, None, None, None,
                   None, ice_cave)
dark_realm = Room("The Dark Realm", 'Your in the dark realm you are where no man dare to seek', None, None, None,
                 ice_cave, None, None, None, Dragon_Shield, )
fall_kingdom = Room("Fallen kingdom runes", 'You are at the runes of the fallen king you may find some of his'
                                           ' treasures', None, None, None, None, None, None,
                   dark_realm, [wifu1, ])
game_room = Room("The Game Dimension", "There are lots of games here", None, None, None, None, frost_forest, None, None,
                wifu2, )
time_room = Room("Time Dimension", 'You are in the time dimension',  None, None, None, None, None, None,
                None, [Longinus_Smasher, wifu3])

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


player = Player(forest)
player.inventory.append(Item)
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
playing = True


while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print()
    print("You have the options to grab these items")
# print(player.current_location.items)
   for item in player.current_location.items:
           print(item.name)

   command = input(">_")

   if command in short_directions:
       pos = short_directions.index(command)
       command = directions[pos]
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

   elif "weeb_bag" in command:
       print("This is whats in your portal")
       print(player.inventory)
       for found_item in player.inventory:
           if found_item is None:
               print("You no have items")
           else:
               print("found_item.name")

   elif "take" in command:
       Item = command[5:]
       ItemInRoom = None
       Name = Item
       for Item in player.current_location.items:
           if Item.name == Item:
               ItemInRoom = Item
           if ItemInRoom is not None:
               player.inventory.append(ItemInRoom)
               player.current_location.Items.remove(ItemInRoom)

   else:
       print("Command no recognized"


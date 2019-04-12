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
        print("Niceo hit")

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


class bodypillow(WearableArmor):
    def __init__(self, name, armor_amt, durability):
        super(bodypillow, self).__init__(name, armor_amt, durability)


class Helmet(WearableArmor):
    def __init__(self, name,  armor_amt, durability):
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
    def __init__(self, name,):
        super(Elixir, self).__init__(name)


class InstantNoodles(Consumable):
    def __init__(self, name,):
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


sword = Weapon("Sword", 10, 100, 1000)
longinus_smasher = Weapon("longinus smasher", 84000, 211111111111111111111100, 1500000000000000000000)
chad_armor = WearableArmor("Armor of the gods", 99999999999999999999, 90000000000000000000000000)

dwarf_king_helm = Helmet("Dwarf King Helmet", 500, 1000)
iron_helm = Helmet("Iron helmet", 500, 1000)
pretty_pegasus = Weapon("Pretty pegasus", 100, 100, 1000)


dragon_shield = Shield("Dragon Shield", 800, 2000)
Iron_shield = Shield("Iron shield", 500, 900)

potion = Consumable("Healing potion")

orc = Character("Orc", 100, sword, WearableArmor("Generic Armor", 1000, 10000000000000))
chad = Character("Chad", 12345678910111213141516171819202122232425262728,longinus_smasher, chad_armor)

orc.attack(chad)
chad.attack(orc)
chad.attack(orc)
orc.attack(chad)

import random
active = True
money = 15
rounds_played = 0
while active and money > 0:
        rounds_played = rounds_played + 1
        dice_2 = random.randint(1, 6)
        dice_1 = random.randint(1, 6)
        print(dice_1 + dice_2)
        if dice_1 + dice_2 == 7:
            money = money + 99999999999
            print("you have won $5. now you have %d " % money)
        else:
            money = money - 1000
            print("you have lost $1 and you now have %d left" % money)

if money <= 0:
        print("you have lost after %d rounds" % rounds_played)
active = False

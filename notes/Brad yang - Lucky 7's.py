import random
active = True
money = 15
rounds_played = 0
while active and money > 0:
    rounds_played = rounds_played + 1
    dice_2 = random.randit(1, 6)
    dice_1 = random.randit(1, 6)
    print(dice_1 + dice_2)
    if dice_1 + dice_2 == 7:
        money = money + 4
        print("you have won $5. now you have %d " % money)
    else:
        money = money -1
        print 



















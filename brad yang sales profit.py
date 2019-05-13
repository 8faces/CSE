import csv


with open("Sales Records.csv", 'r') as csv_file_stuff:
    looker = csv.reader(csv_file_stuff)
    fruit_list = []
    clothes_list = []
    snack_list = []
    office_supplies_list = []
    meat_list = []
    household_list = []
    personal_care_list = []
    cosmetics_list = []
    vegetable_list = []
    cereal_list = []
    beverages_list = []
    baby_food_list = []

    for row in looker:
            region = row[0]
            profit = row[13]  # This is a tring
            fruit = row[2]
            clothes = row[2]
            snack = row[2]
            office_supplies = row[2]
            meat = row[2]
            household = row[2]
            personal_care = row[2]
            cosmetics = row[2]
            vegetable = row[2]
            cereal = row[2]
            beverages = row[2]
            baby_food = row[2]

            if fruit == "Fruits":
                fruit_list.append(float(profit))
                print(region)
                print(fruit)
                print(profit)
                print()
            if clothes == "Clothes":
                clothes_list.append(float(profit))
            if snack == "Snacks":
                snack_list.append(float(profit))
            if office_supplies == "Office Supplies":
                office_supplies_list.append(float(profit))
            if meat == "Meat":
                meat_list.append(float(profit))
            if household == "Household":
                household_list.append(float(profit))
            if personal_care == "Personal care":
                personal_care_list.append(float(profit))
            if cosmetics == "Cosmetics":
                cosmetics_list.append(float(profit))
            if vegetable == "Vegetables":
                vegetable_list.append(float(profit))
            if cereal == "Cereal":
                cereal_list.append(float(profit))
            if beverages == "Beverages":
                beverages_list.append(float(profit))
            if baby_food == "Baby food":
                baby_food_list.append(float(profit))


fruit_sum = sum(fruit_list)
print("The total profit of fruits is %f" % fruit_sum)




print("done")

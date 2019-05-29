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
    sub_saharan_africa = []
    asia = []
    europe = []
    central_america_and_the_caribbean = []
    middle_east_and_north_africa = []
    north_america = []
    australia_and_oceania = []

    for row in looker:
            region = row[0]
            profit = row[13]
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
            sub_saharan_africa = row[2]
            asia = row[2]
            europe = row[2]
            central_america_and_the_caribbean = row[2]
            middle_east_and_north_africa = row[2]
            north_america = row[2]
            australia_and_oceania = row[2]

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
            if personal_care == "Personal Care":
                personal_care_list.append(float(profit))
            if cosmetics == "Cosmetics":
                cosmetics_list.append(float(profit))
            if vegetable == "Vegetables":
                vegetable_list.append(float(profit))
            if cereal == "Cereal":
                cereal_list.append(float(profit))
            if beverages == "Beverages":
                beverages_list.append(float(profit))
            if baby_food == "Baby Food":
                baby_food_list.append(float(profit))
            if sub_saharan_africa == "Sun=Saharan Africa":
                sub_saharan_africa.append(float(profit))
            if asia == "Asia":
                asia.append(float(profit))
            if europe == "Europe":
                europe.append(float(profit))
            if central_america_and_the_caribbean == "Central America and the Caribbean":
                central_america_and_the_caribbean.append(float(profit))
            if middle_east_and_north_africa == "Middle East and North Africa":
                middle_east_and_north_africa.append(float(profit))
            if north_america == "North America":
                north_america.append(float(profit))
            if australia_and_oceania == "Australia and Oceania":
                australia_and_oceania.append(float(profit))

fruit_sum = sum(fruit_list)
clothes_sum = sum(clothes_list)
snack_sum = sum(snack_list)
office_supplies_sum = sum(office_supplies_list)
meat_sum = sum(meat_list)
household_sum = sum(household_list)
personal_care_sum = sum(personal_care_list)
cosmetics_sum = sum(cosmetics_list)
vegetable_sum = sum(vegetable_list)
cereal_sum = sum(cereal_list)
beverages_sum = sum(beverages_list)
baby_food_sum = sum(baby_food_list)
sub_saharan_africa_sum = sum(sub_saharan_africa)
asia_sum = sum(asia)
europe_sum = sum(europe)
central_america_and_the_caribbean_sum = sum(central_america_and_the_caribbean)
middle_east_and_north_africa_sum = sum(middle_east_and_north_africa)
north_america_sum = sum(north_america)
australia_and_oceania_sum = sum(australia_and_oceania)


print("The total profit of fruits is %f" % fruit_sum)
print("The total profit of clothes is %f" % clothes_sum)
print("The total profit of snacks is %f" % snack_sum)
print("The total profit of office supplies is %f" % office_supplies_sum)
print("The total profit of meat is %f" % meat_sum)
print("The total profit of households is %f" % household_sum)
print("The total profit of personal care is %f" % personal_care_sum)
print("The total profit of cosmetics is %f" % cosmetics_sum)
print("The total profit of vegetables is %f" % vegetable_sum)
print("The total profit of beveerages is %f" % beverages_sum)
print("The total profit of baby foods is %f" % baby_food_sum)
print("The total profit of Sub Saharan Africa is %f" % sub_saharan_africa_sum)
print("The total profit of Asia is %f" % asia_sum)
print("The total profit of Europe is %f" % europe_sum)
print("The total profit of Central America and The Caribbean is %f" % central_america_and_the_caribbean_sum)
print("The total profit of Middle East and North Africa is %f" % middle_east_and_north_africa_sum)
print("The total profit of North America is %f" % north_america_sum)
print("The total profit of Australia and Oceania is %f" % australia_and_oceania_sum)

category_sums = [fruit_sum, clothes_sum, snack_sum, office_supplies_sum, meat_sum, household_sum,
                 personal_care_sum, cosmetics_sum, vegetable_sum, beverages_sum, baby_food_sum, ]

category_type = ["Fruit", "Clothes", "Snacks", "Office Supplies", "Meat", "Household", "{Personal Care", "Cosmetics",
                 "Vegetables", "Beverages", "Baby Food"]
index = category_sums.index(max(category_sums))
print("the most profited category is %s " % category_sums[index])

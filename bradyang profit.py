import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    Fruit_Profit = []
    Household_Profit = []
    Office_Supplies_Profit = []
    Clothes_Profit = []
    Meat_Profit = []
    Beverages_Profit = []
    Cosmetics_Profit = []
    Personal_Care_Profit = []
    Baby_Food_Profit = []
    Cereal_Profit = []
    Veggies_Profit = []
    Snacks_Profit = []
    SubSaharan_Africa_Profit = []
    MiddleEastandNorthAfrica_Profit = []
    AustraliaOceania_Profit = []
    Europe_Profit = []
    Asia_Profit = []
    CentralAmericaAndCaribbean_Profit = []
    NorthAmerica_Profit = []
    Fruit_units = []
    Household_units = []
    OfficeSupplies_Units = []
    Clothes_Units = []
    Meat_Unit = []
    Beverages_Units = []
    Cosmetics_Units = []
    PersonalCare_Units = []
    BabyFood_Unit = []
    Cereal_Units = []
    Veggies_Units = []
    Snacks_Units = []
    print("Processing....")
for row in reader:
        Profit = row[13]
        SoldUnits = row[8]
        FRUIT = row[2]
        if FRUIT == "Fruits":
            Fruit_Profit.append(float(Profit))
            Fruit_units.append(int(SoldUnits))
        HOUSEHOLD = row[2]
        if HOUSEHOLD == "Household":
            Household_Profit.append(float(Profit))
            Household_units.append(int(SoldUnits))
        OFFICE_SUPPLIES = row[2]
        if OFFICE_SUPPLIES == "Office Supplies":
            Office_Supplies_Profit.append(float(Profit))
            OfficeSupplies_Units.append(int(SoldUnits))
        CLOTHES = row[2]
        if CLOTHES == "Clothes":
            Clothes_Profit.append(float(Profit))
            Clothes_Units.append(int(SoldUnits))
        MEAT = row[2]
        if MEAT == "Meat":
            Meat_Profit.append(float(Profit))
            Meat_Unit.append(int(SoldUnits))
        BEVERAGES = row[2]
        if BEVERAGES == "Beverages":
            Beverages_Profit.append(float(Profit))
            Beverages_Units.append(int(SoldUnits))
            COSMETICS = row[2]
        if COSMETICS == "Cosmetics":
            Cosmetics_Profit.append(float(Profit))
            Cosmetics_Units.append(int(SoldUnits))
        PERSONAL_CARE = row[2]
        if PERSONAL_CARE == "Personal Care":
            Personal_Care_Profit.append(float(Profit))
            PersonalCare_Units.append(int(SoldUnits))
        BABY_FOOD = row[2]
        if BABY_FOOD == "Baby Food":
            Baby_Food_Profit.append(float(Profit))
            BabyFood_Unit.append(int(SoldUnits))
        CEREAL = row[2]
        if CEREAL == "Cereal":
            Cereal_Profit.append(float(Profit))
            Cereal_Units.append(int(SoldUnits))
        VEGGIES = row[2]
        if VEGGIES == "Vegetables":
            Veggies_Profit.append(float(Profit))
            Veggies_Units.append(int(SoldUnits))
        SNACKS = row[2]
        if SNACKS == "Snacks":
            Snacks_Profit.append(float(Profit))
            Snacks_Units.append(int(SoldUnits))
        SUBSAHARAN = row[0]
        if SUBSAHARAN == "Sub-Saharan Africa":
            SubSaharan_Africa_Profit.append(float(Profit))
        MIDDLEEASTANDNORTHAFRICA = row[0]
        if MIDDLEEASTANDNORTHAFRICA == "Middle East and North Africa":
            MiddleEastandNorthAfrica_Profit.append(float(Profit))
        AUSTRALIAOCEANIA = row[0]
        if AUSTRALIAOCEANIA == "Australia and Oceania":
            AustraliaOceania_Profit.append(float(Profit))
        EUROPE = row[0]
        if EUROPE == "Europe":
            Europe_Profit.append(float(Profit))
        ASIA = row[0]
        if ASIA == "Asia":
            Asia_Profit.append(float(Profit))
        CENTRALAMERICAANDCARIBBEAN = row[0]
        if CENTRALAMERICAANDCARIBBEAN == "Central America and the Caribbean":
            CentralAmericaAndCaribbean_Profit.append(float(Profit))
        NORTHAMERICA = row[0]
        if NORTHAMERICA == "North America":
            NorthAmerica_Profit.append(float(Profit))
        Unit_AverageFruit = row[8]
SnacksUnit_Total = sum(Snacks_Units)
    VeggiesUnits_Total = sum(Veggies_Units)
    CerealUnit_Total = sum(Cereal_Units)
    BabyFoodUnit_Total = sum(BabyFood_Unit)
    PersonalCareUnits_Total = sum(PersonalCare_Units)
    CosmeticsUnits_Total = sum(Cosmetics_Units)
    BeveragesUnits_Total = sum(Beverages_Units)
    MeatUnits_Total = sum(Meat_Unit)
    ClothesUnits_Total = sum(Clothes_Units)
    OfficeSuppliesUnits_Total = sum(OfficeSupplies_Units)
    HouseholdUnits_Total = sum(Household_units)
    FruitUnits_Total = sum(Fruit_units)
    NorthAmerica_sum = sum(NorthAmerica_Profit)
    Asia_sum = sum(Asia_Profit)
    CentralAmericaAndCaribbean_Sum = sum(CentralAmericaAndCaribbean_Profit)
    Europe_sum = sum(Europe_Profit)
    AustraliaOceania_sum = sum(AustraliaOceania_Profit)
    MiddleEastandNorthAfrica_sum = sum(MiddleEastandNorthAfrica_Profit)
    SubSaharan_Africa_sum = sum(SubSaharan_Africa_Profit)
    Snacks_sum = sum(Snacks_Profit)
    Veggies_sum = sum(Veggies_Profit)
    Cereal_sum = sum(Cereal_Profit)
    Baby_Food_sum = sum(Baby_Food_Profit)
    Personal_Care_sum = sum(Personal_Care_Profit)
    Cosmetics_sum = sum(Cosmetics_Profit)
    Beverages_sum = sum(Beverages_Profit)
    Meat_sum = sum(Meat_Profit)
    Clothes_sum = sum(Clothes_Profit)
    Office_Supplies_sum = sum(Office_Supplies_Profit)
    Household_sum = sum(Household_Profit)
    Fruit_Sum = sum(Fruit_Profit)
FruitAverageUnits = Fruit_Sum / FruitUnits_Total
    Household_units = Household_sum / HouseholdUnits_Total
    OfficeSupplies_Units = Office_Supplies_sum / OfficeSuppliesUnits_Total
    Clothes_Units = Clothes_sum / ClothesUnits_Total
    Meat_Unit = Meat_sum / MeatUnits_Total
    Beverages_Units = Beverages_sum / BeveragesUnits_Total
    Cosmetics_Units = Cosmetics_sum / CosmeticsUnits_Total
    PersonalCare_Units = Personal_Care_sum / PersonalCareUnits_Total
    BabyFood_Unit = Baby_Food_sum / BabyFoodUnit_Total
    Cereal_Units = Cereal_sum / CerealUnit_Total
    Veggies_Units = Veggies_sum / VeggiesUnits_Total
    Snacks_Units = Snacks_sum / SnacksUnit_Total
ItemCategorySum = [Fruit_Sum, Household_sum, Office_Supplies_sum, Clothes_sum, Meat_sum, Beverages_sum,
                       Cosmetics_sum, Personal_Care_sum, Baby_Food_sum, Cereal_sum, Veggies_sum, Snacks_sum]

    RegionProfitSum = [SubSaharan_Africa_sum, MiddleEastandNorthAfrica_sum, AustraliaOceania_sum, Europe_sum,
                       CentralAmericaAndCaribbean_Sum, Asia_sum]

    RegionOfProfit = ["Sub-Saharan Africa", "Middle East and North Africa", "Australia and Oceania", "Europe",
                      "Asia", "Central America and the Caribbean", "North America"]

    ItemCategoryType = ["Fruit", "Household", "Office Supplies", "Clothes", "Meat", "Beverages", "Cosmetics",
                        "Personal Care", "Baby Care", "Cereal", "Vegetables", "Snacks"]

    index = ItemCategorySum.index(max(ItemCategorySum))
    index2 = RegionProfitSum.index(max(RegionProfitSum))
print("The average amount of Money per Unit in the Fruit Category is %f" % FruitUnits_Total)
    print("The average amount of Money per Unit in the Household category is %f" % HouseholdUnits_Total)
    print("The average amount of Money per Unit in the Office Supply category is %f" % OfficeSuppliesUnits_Total)
    print("The average amount of Money per Unit in the Clothes Category is %f" % ClothesUnits_Total)
    print("The average amount of Money per Unit in the Meat Category is %f" % MeatUnits_Total)
    print("The average amount of Money per unit in the Beverage category is %f" % BeveragesUnits_Total)
    print("The average amount of Money per unit in the Cosmetics category is %f" % CosmeticsUnits_Total)
    print("The average amount of Money per unit in the Personal Care Category is %f" % PersonalCareUnits_Total)
    print("The average amount of Money per unit in the Baby Food Category is %f" % BabyFoodUnit_Total)
    print("The average amount of Money per unit in the Cereal Category is %f" % CerealUnit_Total)
    print("The average amount of Money per unit in the Veggies Category is %f" % VeggiesUnits_Total)
    print("The average amount of Money per unit in the Snacks Category is %f" % SnacksUnit_Total)
    print()
    print()
print("THE TOTAL AMOUNT OF PROFIT THE FRUIT CATEGORY IS %f" % Fruit_Sum)
    print("THE TOTAL AMOUNT OF PROFIT THE HOUSEHOLD CATEGORY IS %f" % Household_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE OFFICE SUPPLY CATEGORY IS %f" % Office_Supplies_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE CLOTHES CATEGORY IS %f" % Clothes_sum)
    print("THE TOTAL AMOUNT OF PROFIT THE MEAT CATEGORY IS %f" % Meat_sum)
    print("The total amount of profit the beverage category has is %f" % Beverages_sum)
    print("The total amount of profit that the Cosmetics Category made is %f" % Cosmetics_sum)
    print("The total amount of profit the Personal Care category made is %f" % Personal_Care_sum)
    print("The Total amount of profit the Baby Food category made is %f" % Baby_Food_sum)
    print("The total amount of profit the Cereal Category made is %f" % Cereal_sum)
    print("The total amount of profit the Vegetables category made is %f" % Veggies_sum)
    print("The total amount of Profit the Snacks Category made is %f" % Snacks_sum)
    print("AND The Category with the MOST AMOUNT OF PROFIT is....... %s!!!!!!!!!!!!!!!!" % ItemCategoryType[index])
    print()
    print()
print("New List about the profit from Regions.")
    print("The total Profit of the Sub Saharan Africa Region is % f" % SubSaharan_Africa_sum)
    print("The total profit of the Middle East and North Africa region is %f" % MiddleEastandNorthAfrica_sum)
    print("The total Profit of the Australia And Oceania region is %f" % AustraliaOceania_sum)
    print("The total amount of Profit the Europe region is %f" % Europe_sum)
    print("The total amount of Profit the Asia region has is %f" % Asia_sum)
    print("The total amount of Profit the Central America and Caribbean region is %f" % CentralAmericaAndCaribbean_Sum)
    print("The total amount of Profit North America made is %f" % NorthAmerica_sum)
    print("AND the Region with the Most amount of profit is (DRUMROLL).... %s!!!!!!!" % RegionOfProfit[index2])
    print("Done")
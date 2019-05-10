import csv


with open("Sales Records.csv", 'r') as csv_file_stuff:
    looker = csv.reader(csv_file_stuff)

    for row in looker:
            region = row[0]
            profit = row[13]  # This is a string
            fruit = row[2]
            clothes = row[2]
            snack = row[2]
            office_supplies = row[2]
            if fruit == "Fruits":
                print(region)
                print(fruit)
                print(profit)
                print()



            if clothes == "Clothes":


                if fruit == "Snacks":


                    if fruit == "Office Supplies":




print("done")

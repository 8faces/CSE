import csv


with open("Sales Records.csv", 'r') as csv_file_stuff:
    looker = csv.reader(csv_file_stuff)

    for row in looker:
            profit = row[13]  # This is a string
            fruit = row[2]
            if fruit == "Fruits":
                print(fruit)
                print(profit)



import csv


def validate1(num: str):
    if stuff(num) and validate(num):
        return True
    return False


def validate(num: str):
    first_num = int(num[0])
    if first_num % 3 == 1:
        return True
    return False


def stuff(num: str):
    first_num = int(num[1])
    if first_num % 2 == 0:
        return True
    return False

# # print(int(old_number)+1)
# import csv
#
# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = row[0]
#         print(old_number)
# # print(int(old_number)+1)
# import csv
#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("processing")
#
#         for row in reader:
#
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num == 4:
#                 writer.writerow(row)
#         print("Done")
#
#
# # print(int(old_number)+1)


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("Done")

test_num = "3586782824154010"


def validate(num: str):
    number_list = list(num)
    print(number_list)
    last_num = int(number_list.pop(15))
    print(number_list)
    print(last_num)
    number_list = reverse_it(number_list)
    print(number_list)


def reverse_it(number_list: list):
    number_list = number_list[::-1]
    return number_list


def multiply_by_2_subtracting_9(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9


def mod_TEN

print(validate(test_num))


# print(revers_it("olleh dlrow"))
#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file...   ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]  # This is a string
#             if validate(old_number):
#                 writer.writerow(row)
#         print("done")
#

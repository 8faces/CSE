import csv


def validate(num: str):
    number_list = list(num)
    last_number = int(number_list[15])
    number_list.pop(15)
    number_list = reverse(number_list)
    multiply_and_subtract(number_list)
    total_sum = sum(number_list)
    return mod_ten(total_sum, last_number)


def reverse(string):
    string = string[::-1]
    return string


def multiply_and_subtract(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])    # Goes and looks at the even numbers
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9


def mod_ten(total_sum, last_number):
    if int(total_sum) % 10 == int(last_number):
        return True
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing....")
        for row in reader:
            num = row[0]     # A String object
            if validate(num):
                writer.writerow(row)

# for index in range(len(num)):

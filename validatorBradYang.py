import csv

test_num = "3586782824154010"


def validate(num: str):
    for index in range(len(num)):
        int_version = int(num(index))

        
print(validate(test_num))


def revers_it(string):
    return string[::-1]


print(revers_it("olleh dlrow"))

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...   ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]  # This is a string
            if validate(old_number):
                writer.writerow(row)
        print("done")


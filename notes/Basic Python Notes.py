
print("Hello World!")

# Apparely i'm going to slow.,slow, so i will speed up
# This is a comment
# This has no effect on the code
# # This is used for a variety of things, such as
# # 1. making personal notes about my code
# # 2.commenting out code that dose not work
#
# print("Notice what is happening here.")
# print()  # this creates a new line
# print()  # Do you notice the underline here?
# # Hover over top it to see what is wrong.
#
# # math
print(5+3)
print(5-3)
print(4*5)
print(6/5)
print()

# semi-advanced math
print("figure this out...")
print(6//4)
print(12//3)
print(9//4)  # THis will ONLY give me a whole number
print()

print("figure this out too...")
print(6%4)
print(5%3)
print(9%4)

# Defining variables
car_name = "Wiebe mobile" # string
car_type = "tesla" # string
car_cylinders = 16 # integer
car_miles_per_gallon = 0.01 # float

print("I have a car called %s. It's pretty nice"% car_name)
print("It has %d cylinders, but gets %f mpg" % (car_cylinders, car_miles_per_gallon))

# Taking Input
name = input("what is your name?")
print("Hello %s" % name)

age = input("How old are you?")
print("%s? You belong in a museum" % age)

# Recasting
real_age = (input ("how old are you again?"))
hidden_age = real_age + 5
print(hidden_age)


# Multi-line Comments

"""
This is a multi-line comment
anything in between them is automatically commented
"""


# Defining Functions
def say_it():
    print("hello world")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# For loops
for i in (1,2,3):
    say_it()

for i in range(5):  # range (5 gives the number 0-4
    f(i)

for i in range(5):
    print(i**2)

# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as a a+1


"""
hints for loops:
For Loops - Use when you Know EXACTLY how many iterations
while loops - use when you don't know how many iterations
"""

# control Statements (if statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc (percentage):
    if percentage >=90:
        return "A"
    elif percentage >= 80:
        return "b"
    elif percentage >= 70:
        return "c"
    elif percentage >= 60:
        return "d"
    else:
        return "f"



your_grade = grade_calc(82)
print(your_grade)

# Random numbers
import random
print(random.randint(0, 100))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3 # A is set to 3
a==3 # is a equal to 3?
"""


# function notes
# a**2 + b**2 = c**2


def pythagorean(a, b):
    return (a**2 + b**2) ** (1/2)


print(pythagorean(3, 4))




"""
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
"""

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

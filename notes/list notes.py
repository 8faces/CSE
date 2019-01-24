

# Creating a list
fruit = ['apples', 'oranges', 'grapes',
         'mango', 'pineapple', 'strawberries', 'banana', 'pees', 'tomato', ]    # USE SQUARE BRACKETS!!!!!!!!!
print(fruit)

# Pulling items from a list
print(fruit[1])

# getting length of a list
print(len(fruit))
print("the length of the list is %d" % len(fruit))

# modifying list
fruit[8] = 'coconut'
print(fruit)

# looping through lists
for item in fruit:
    print(item)



Hero1 = ['genji', 'soldier_76', 'winston', 'Reaper', 'tracer', 
        'wreaking_ball', 'Dva', 'hanzo', 'mercy', 'junk_rat']

print(" The last thing in the list is %s" % Hero1[len(Hero1)-1])










Hero = ['genji', 'soldier_76', 'winston', 'Reaper', 'tracer',
        'wreaking ball', 'chicken', 'Dva', 'hanzo', 'mercy', 'junk_rat', 'widowmaker', 'maccree']


print(Hero[2:5])
print(Hero[3:4])
print(Hero[10:])
print(Hero[:5])

# adding stuff to a list (part 1)

Hero.append("lulu")
Hero.append("garen")
print(Hero)

# Addding to a list (no at the end)
Hero.insert(2, "shaco")
print(Hero)

Hero.remove("hanzo")
Hero.remove("genji")
print(Hero)

# Removing from a list (pt 2)
# sometimes, you don't know what is in the list, but you know
# you want to get rid of something at a specific index
Hero.pop(0)
print(Hero)
# notice that soldier_76 is no longer in the list because was is at index 0


number_list = ['1', '2', '3', '4', '5', '6', '7', '8', ]

print(number_list[1:])
print(number_list[2:])
print(number_list[3:])

number_list.insert(4, "4")

number_list.remove("3")
print(number_list)

# avoid putting parentheses when making a list


# changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list)

for i in range(len(list1)):
        if list1[i] == "u":     # i goes through all indices
            list1.pop(i) # if you find a "u"
            list1.insert(i, " censor ")       # remove the i_th index
# put a censor in there instead
print("".join(list1))


import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

bill_roll = (names[random.randint(0, len(names)-1)])
print(f"{bill_roll} is going to buy the meal today!")
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

size_price = 0
pepperoni_price = 0
cheese_price = 0

if size == "S":
    size_price = 15
    if add_pepperoni == "Y":
        pepperoni_price += 2
    elif extra_cheese == "Y":
        cheese_price += 1

if size == "M":
    size_price = 20
    if add_pepperoni == "Y":
        pepperoni_price += 3
    elif extra_cheese == "Y":
        cheese_price += 1

if size == "L":
    size_price = 25
    if add_pepperoni == "Y":
        pepperoni_price += 3
    elif extra_cheese == "Y":
        cheese_price += 1

final_bill = size_price + pepperoni_price + cheese_price

print(f"Your final bill is: ${final_bill}")

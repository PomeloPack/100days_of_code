height = int(input("What is your current height in cm? "))
bill = 0

if height >= 120:
    print("You can ride to rollercaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("You paid $5 for entry")
    elif age <= 18:
        bill = 7
        print("You paid $7 for entry")
    else:
        bill = 12
        print("You paid $12 for entry")
    
    photo = input("Do you want a photo of your ride? Y for yes or N for no: ")
    
    if photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
    elif photo == "y":
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill without photo is ${bill}")

    
else:
    print("Sorry, you have to grow taller before you can ride.")

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's leap year.")
        else:
            print("It isn't leap year.")
    else:
        print("It's leap year")
else:
    print("It ins't leap year")


"""input 2

if year % 4 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")"""
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill ? \n$"))
percentage_tip = int(input("What % tip would you like to give ? 10, 12 or 15?\n%"))
people_split = int(input("How many people to split the bill?\n"))

pay_per_ppl = (round(float(((percentage_tip / 100 * total_bill) + total_bill) / people_split), 2))

print(f"Each person should pay: ${pay_per_ppl}")






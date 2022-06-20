age = input("What is your current age?")

year_days = 365 * 90
year_weeks = 52 * 90
year_months = 12 * 90

print(f"You have {year_days - int(age) * 365} days, {year_weeks - int(age) * 52} weeks, and {year_months - int(age) * 12} months left") 
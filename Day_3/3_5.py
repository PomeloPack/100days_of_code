print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_together = name1 + name2
lower_names = names_together.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")


true = t + r + u + e
love = l + o + v + e

total_score = int(str(true) + str(love))


if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")

elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you'r alright together.")

else:
    print(f"Your score is {total_score}.")










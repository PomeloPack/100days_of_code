import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

"""
0 = rock
1 = paper
2 = scissors
"""

user_choice = input("What do you choose?\n\nType:\n\n0 for rock\n\n1 for Paper\n\n2 for Scissors\n\nChoose here: ")

if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("This option is wrong! Try again.")

print("Computer choose: ")

computer_choice = random.choice([rock, paper, scissors])

if computer_choice == rock:
    print(rock)
elif computer_choice == paper:
    print(paper)
elif computer_choice == scissors:
    print(scissors)



if user_choice == computer_choice:
    print("This game is tie!")
elif(user_choice == "0" and computer_choice == scissors):
    print("User win over computer!")
elif(user_choice == "0" and computer_choice == paper):
    print("Computer win over user!")
elif(user_choice == "1" and computer_choice == rock):
    print ("User win over computer!")
elif(user_choice == "1" and computer_choice == scissors):
    print("Computer win over user!")
elif(user_choice == "2" and computer_choice == paper):
    print("User win over computer!")
elif(user_choice == "2" and computer_choice == rock):
    print("Computer win over user!")
else:
    print("This option is wrong! Try again.")








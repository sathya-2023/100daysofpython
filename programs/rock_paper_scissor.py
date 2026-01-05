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

game_choices = [rock,paper,scissors]

user_choice = int(input("Enter your choice: 0 for Rock, 1 for Scissor and 2 for Paper \n" ))
print(game_choices[user_choice])

comp_choice = random.randint(0,2)
print("Computer choice: \n")
print(game_choices[comp_choice])

if user_choice >= 3 or user_choice < 0:
    print("Choose a correct choice")
elif user_choice == 0 and comp_choice == 2:
    print("You Win")
elif comp_choice == 0 and user_choice == 2:
    print("You lose")
elif user_choice < comp_choice:
    print("You lose")
elif user_choice == comp_choice:
    print("It's a draw")
elif user_choice > comp_choice:
    print("You win")
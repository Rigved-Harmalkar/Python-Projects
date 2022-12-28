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
picture = [rock, paper, scissors]
user = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(picture[user])
computer_choice = random.randint(0,2)
print(f"computer chose:")
print(picture[computer_choice])
if user==0 and computer_choice ==2:
    print("You win!")
elif computer_choice==0 and user==2:
    print("you lose!")
elif user>computer_choice:
    print("You win!")
elif computer_choice > user:
    print("You lose!")

elif user==computer_choice:
    print("game tied")
elif user>=3 or user<0:
    print("you lose,invalid choice")

else:
    print("invalid choice!")

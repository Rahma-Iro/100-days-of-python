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
inputs_list = random.randint(0, 2)
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))
print("you chose:")
print(game_images[player_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])
if player_choice == computer_choice:
    print("draw")
elif player_choice == 0  and computer_choice == 1:
    print("opps!! paper covers rock you loose!!")
elif player_choice == 0  and computer_choice == 2:
    print("yayyy!! rock crushes scissors you win!!")
elif player_choice == 2  and computer_choice == 1:
    print("yayy!! scissors cuts paper you win!!")
else:
    print("you loose!!!")


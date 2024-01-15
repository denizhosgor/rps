import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

list = [rock,paper,scissors]
list_rand_num = random.randint(0,len(list)-1)
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if selection > 2:
    print("You lose :(")
else:
    print(list[selection])

    print("Computer chose:")
    print(list[list_rand_num])

    if list[selection] == list[list_rand_num]:
        print("Draw  :S")
    elif (list[selection] == rock and list[list_rand_num] == paper) or (list[selection] == paper and list[list_rand_num] == scissors) or (list[selection] == scissors and list[list_rand_num] == rock):
        print("You lose :(")
    elif (list[selection] == rock and list[list_rand_num] == scissors) or (list[selection] == paper and list[list_rand_num] == rock) or (list[selection] == scissors and list[list_rand_num] == paper):
        print("You win :)")



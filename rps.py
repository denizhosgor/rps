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
input_sel = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if not input_sel.isdigit():
    if not isinstance(input_sel,int):
        print("You can not use letter only numbers.\n")
else:
    selection = int(input_sel)
    if int(input_sel) > 2:
        print("You have only 3 selection not other numbers.\n")
    else:
        print(list[selection])

        print("Computer chose:")
        print(list[list_rand_num])

        if list[selection] == list[list_rand_num]:
            print("Draw  :S\n")
        elif (list[selection] == rock and list[list_rand_num] == paper) or (list[selection] == paper and list[list_rand_num] == scissors) or (list[selection] == scissors and list[list_rand_num] == rock):
            print("You lose :(\n")
        elif (list[selection] == rock and list[list_rand_num] == scissors) or (list[selection] == paper and list[list_rand_num] == rock) or (list[selection] == scissors and list[list_rand_num] == paper):
            print("You win :)\n")

import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Weapon =["Rock", "Paper", "Scissors"]
Game_Image = [Rock,Paper,Scissors]
Computer_Weapon = random.randint(0,2)
Computer_selection = Weapon[Computer_Weapon]
Computer_Image = Game_Image[Computer_Weapon]

print("Welcome To the Rock,Paper & Scissors Game")
Age_Confirmation=input("Please confirm you are over 3 years old (Yes or No)\n").lower()

if Age_Confirmation== "yes" or Age_Confirmation=="yh" or Age_Confirmation=="yeah" or Age_Confirmation=="y":


    Selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    User_Selection_Choice = Weapon[Selection]#here this helps to capture the users choice as a number and associate it with the list because selction will be a number and then in square brackets it targets from the list
    User_Image = Game_Image[Selection]


    if User_Selection_Choice== "Rock":
        print(f'You selected Rock: {User_Image} \nThe Computer selected {Computer_selection}:') #didnt need to use f string but good practice
        if Computer_selection == Weapon[0]:
            print(Computer_Image+ "\nRock Vs Rock is a draw")
        elif Computer_selection == Weapon[1]:
            print(Computer_Image+ "\nRock Vs Paper, You lose")
        else:
            print(Computer_Image+ "\nRock vs Scissors, You win")


    elif User_Selection_Choice== "Paper":
        print(f'You selected Paper: {User_Image} \nThe Computer selected {Computer_selection} :')
        if Computer_selection == Weapon[0]:
            print(Computer_Image+ "\nPaper vs Rock,You win" )
        elif Computer_selection == Weapon[1]:
            print(Computer_Image+ "\nPaper Vs Paper is a Draw")
        else:
            print(Computer_Image+ "\nPaper Vs Scissors,You Lose")


    else:
        print(f'You selected Scissors: {User_Image} \nThe Computer selected {Computer_selection}:')
        if Computer_selection == Weapon[0]:
            print(Computer_Image+"\nScissors vs Rock,You Lose")
        elif Computer_selection==Weapon[1]:
            print(Computer_Image+"\nScissors Vs Paper, You win")
        else:
            print(Computer_Image+"\nScissors Vs Scissors is a Draw")


else:
    print("Sorry,You are not eligible to play the game")

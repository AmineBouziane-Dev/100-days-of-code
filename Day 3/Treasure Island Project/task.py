print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Name = input("What is your Name?")
print("Assalamualaikum " + Name)
Start_Game=input("Are you ready to start?").lower()
if Start_Game != "yes":
    print("Thank you for playing See you next time!")
else:
    print("Say BismiAllah, Lets begin:")

Step1 = input("You are at the first checkpoint " + Name + " would you like to go Left or Right?\n").lower()
if Step1=="right":
    print("You have reached the next stop " + Name + ",you are at the ocean.")
    Step2=input("Would you like to Swim or Wait?\n").lower()
    if Step2=="wait":
        print("Prophet Muhammad ﷺ said: Patience is a light.(Sahih Muslim)\nWell done for being patient,A dolphin came and saved you, you have reached the next stage!")
        Step3= input("Pick the right answer to move to the next stage.I am a Prophet who was thrown into a well as a child. Who am I?\n").lower()
        if Step3 == "yusuf" or Step3 ==  "yousuf" or Step3 == "yousif" or Step3=="yousef" or Step3=="yosef" or Step3=="yosif" or Step3=="yusif":
            print("You have reached the last stage of the game, you are currently standing on a field, you must answer this question to have access to the Treasure")
            Final_stage1=input("Who is your lord?").lower()
            Final_Stage2=input("Who is your messenger?").lower()
            if Final_stage1 =="allah" and (Final_Stage2=="mohammed" or Final_Stage2=="Muhammed" or Final_Stage2=="muhamed" or Final_Stage2=="mohamed"): #you will learn about using "in" later on to make it look more clean
                print( "✨ Masha’Allah! You answered with the truth — Allah is your Lord and Muhammad ﷺ is His Messenger. May Allah bless you with success and happiness. You win the treasure! Now look behind the laptop for your treasure!")


            else:
                print("You have lost the game, no treasure for you")

        elif Step3 =="red":
            print("Game Over!You walked into an explosion")
        elif Step3 =="pink":
            print("Game Over")
        else:
            print("Game Over!")



    else:
        print("Game Over! You were attacked by sharks")




else:
    print("Game Over! You have fallen into a hole ")
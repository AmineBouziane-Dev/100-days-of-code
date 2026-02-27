Age=input("what is your age?")
Odd_Even_Age  = int(Age)%2 #have to put int here because remember the age input will be a string text form, input is always in string form.
if Odd_Even_Age == 0:
    print(f"Your age {Age} is Even!")
else:
    print(f"Your age {Age} is Odd!")

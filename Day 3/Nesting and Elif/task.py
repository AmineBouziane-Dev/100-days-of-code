print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are eligible for the rollercoaster")
    Age = int(input("What is your Age?"))
    if Age <= 12:
        print("You May enter the ride for free")
    elif Age <=15:
        print("Please pay £15")
    else:
        print("Please pay £25")
elif height <120:
    PG_Present = input("Are you with your parents/Guardian?")
    if PG_Present == "yes":
        print("You May enter the ride with your Parent Guardian")
        Age = int(input("What is your Age?"))
        if Age <= 12:
            print("You May enter the ride for free")
        elif Age <= 15:
            print("Please pay £15")
        else:
            print("Please pay £25")

    else:
        print("Sorry you are not eligible")



else:
    print("Sorry you have to grow taller before you can ride.")

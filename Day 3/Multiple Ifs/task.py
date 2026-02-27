print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child Tickets are $5.")
        bill=5
    elif age <= 18:
        print("Youth Tickets are $7.")
        bill=7
    else:
        print("Adult Tickets are $12.")
        bill=12
    Photo = input("Would you like a photo taken?(additional fees apply) ")
    if Photo == "yes":
        bill+=3 #this allows plus 3 to whatever bill value is elected
    else:
        bill=bill #dont need to include this but did just for understanding
    print("Your final bill is $"+ str(bill))
#or i could use f string which is : print(f"your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")


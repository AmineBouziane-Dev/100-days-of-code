

def greet(xyz):
    print(f"Hello {xyz}")
    print(f"Nice to meet you {xyz}")

greet("amine")

#coding exercise 7
age = int(input("How old are you?"))


def life_in_weeks(user_age): #so here the parameter is user age and the argument is age so when running through the function everyplace userage is mentioned it is replaced by the variale age or it could be a string etc etc
    weeks_lived = user_age * 52
    ninety_years = 90 * 52
    ninety_years-=weeks_lived
    print(f'You have {ninety_years} weeks left.')


life_in_weeks(age)
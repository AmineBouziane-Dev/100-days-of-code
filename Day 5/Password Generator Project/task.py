import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password="" # could have used password =[] to make sure everything is a list not string to begin with and avoid using list() later to convert to list as shuffle only works on lists, but good practice to convert to list
for selection_Letters in range(0, nr_letters): #can use range(1, nr_letters+1) instead of doing the 0 gives the same range
    password+= random.choice(letters)
for selection_symbols in range(0,nr_symbols):
    password+=random.choice(symbols)
for selection_numbers in range(0,nr_numbers):
    password+=random.choice(numbers)

password_as_list=list(password) #Function	What it does is make a list or put things in list form
random.shuffle(password_as_list)#cant assign a variable directly to shuffle that isnt a list or other forms (cant be a string or tuple things that cant be changed via appending) e.g new_password=random.shuffle(shuffled_password) doesnt work, the shuffled part just literally shuffles the list you want then you can print out that same list after
new_password=''.join(password_as_list)#use join here because the list you just shuffled will be printed as a list otherwise
print(new_password)




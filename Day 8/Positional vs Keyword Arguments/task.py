# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

#Functions with more than 1 input


# user_location=input("what is your location?")
# user_name=input("what is your name?")
#
# def greet_with(name,location):
#     print(f'Hello {name}')
#     print(f'What is it like in {location}')
#
# greet_with("amine","cardiff")
# greet_with(user_name,user_location)


#Love score udemy exercise
def calculate_love_score(name_1,name_2):
    word_count=0
    word_count_2=0
    for letter in name_1:
        if letter in "true":
            word_count+=1
        if letter in "love":
            word_count_2+=1
    for letter_2 in name_2:
        if letter_2 in "true":
            word_count+=1
        if letter_2 in "love":
            word_count_2+=1

    print(f'Love Score = {word_count}{word_count_2}')


calculate_love_score("kanye west","kim kardashian")


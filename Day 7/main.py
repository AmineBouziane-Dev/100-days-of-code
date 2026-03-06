import random

import hangman_art
import hangman_words
#introduction
print(hangman_art.logo)
name=input("Welcome to the hangman game, What is your name?\n")

word_to_guess=random.choice(hangman_words.word_list) #like we learned on day 4 for modules must use a dot.(see notes)
#here I need to print out the word but use _ in each spot
length_of_word=len(word_to_guess)
guess_display="" #remember we need this out here as the loop resets everytime and we need it to save each time or else guess display would be empty
for letter in range(0,length_of_word):
    guess_display+="_"
print(f"The word to guess is: {guess_display}")

print(f"Your Chosen word is {length_of_word} letters,let the games begin, No pressure {name}.")

#next stage is the big loop that affects lives and goes through the word

lives = 6
saved_letters=[]
used_letters=[]



while guess_display!=word_to_guess and lives!=0:
    guess_display=""

    user_guess=input("Guess a letter:").lower()
    for letter in word_to_guess:
        if letter in saved_letters:
            guess_display+=letter
        elif user_guess == letter:
            guess_display+=user_guess

        else:
            guess_display+="_"




    if user_guess in word_to_guess and user_guess not in saved_letters:
        print(f"correct the letter {user_guess} is in the word.")
        if lives == 1:
            print(f"***************************** YOU HAVE {lives} LIFE LEFT *****************************")
        else:
            print(f"***************************** YOU HAVE {lives} LIVES LEFT *****************************")

        print(hangman_art.stages[lives])
        used_letters+=user_guess
        saved_letters += user_guess

    elif user_guess in saved_letters or user_guess in used_letters:
        print(f"You've already used the letter {user_guess} ")


    else:
        lives-=1
        print(f"incorrect the letter {user_guess} is NOT in the word.")
        if lives == 1:
            print(f"***************************** YOU HAVE {lives} LIFE LEFT *****************************")
        else:
            print(f"***************************** YOU HAVE {lives} LIVES LEFT *****************************")

        print(hangman_art.stages[lives])
        used_letters+=user_guess






#this part of the loop either ends the game winner/loser or recycles by giving what's left of the word then you go again
    if lives==0:
        print(f"Game Over the word was {word_to_guess} {hangman_art.loser}")
    elif guess_display==word_to_guess:
        print(f"You Win{hangman_art.trophy}")
    else:
        print(f"Word to guess: {guess_display}")

# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
other = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\',
         ']', '^', '_', '`', '{', '|', '}', '~', '"', "'"]



    # TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, user_direction):
    new_position = []
    new_text = ''
    for letters in text:
        if letters in alphabet:
            original_position = alphabet.index(letters)
            if direction == "encode":
                new_position = original_position + shift_amount
            elif direction == "decode":
                new_position = original_position - shift_amount

            new_position %= len(alphabet) # I originally was going to put these two under each if and elif statement (encode or decode) but i realised its the same for both so dont need to
            new_text += alphabet[new_position]


        elif letters in other:
            new_text+=letters

    print(f'The {direction}d word is: {new_text}')




user_retry=True #this is a good technique to come in handy make note
#don't need to do == TRUE can just write while user_retry: for simplification but im keeping it to understand my own code for now
while user_retry==True: #initially made a mistake her using one equals, remember double equals is to check something and is perfect for loops/if statements etc, single equals makes it that value exactly
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction !="encode" and direction !="decode":
        print("Invalid input, please try again")
        continue# learned this new - restarts the loop, need to go over break aswell as return but havent been covered yet so comeback once learned
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,user_direction=direction)
    user_retry= input("Would you like to go again? (yes or no)\n").lower()

    if user_retry =="no":
        user_retry=False
        print("Thank you,Bye")
    else:
        user_retry=True #don't really need to include this, but I am, so I understand the logic

#issues I haven't accounted for - when someone types something that isnt an integer for shift what happens or they type a decimal

    # TODO-3: Can you figure out a way to restart the cipher program?





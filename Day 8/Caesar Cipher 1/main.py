alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text,shift_amount): #I should use parameters and take inputs outside of function for a cleaner code, its a rule of thumb to help with testing later on.

    encrypted_word=""
    for letters in original_text:
        original_position=alphabet.index(letters)

        new_position=(original_position+shift_amount) # here we did the modulo technique to avoid the shift being out of range, for example the word zoo with shift above 0 will be out of range e.g 9 would mean 26+9=34 and there is no position 34 so modulo on the max value (26 letters) helps keep it in range which would be position 8, thats a rule of thumb, modulo of max value
        # A better thing would be to do modulo length of list as the list may change and not be 26
        #another thing you can do to make code look cleaner is %= which is the same as += so new_position%=26 or len(alphabet)
        new_position%=26
        new_letters=alphabet[new_position]

        encrypted_word+=new_letters


    print(encrypted_word)




encrypt(original_text=text,shift_amount=shift)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


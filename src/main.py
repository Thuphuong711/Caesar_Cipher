alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        # the code below is for testing
        # print(f"index of letter {letter} is {letter_index}")

        # this is the index after shifting forward
        new_index = letter_index + shift

        # check if the new index is greater than the length of the alphabet -> to avoid   List Index Out of Range error
        if new_index >= len(alphabet):
            num = int(new_index / len(alphabet))
            new_index -= len(alphabet) * num
        encrypted_text += alphabet[new_index]
        # the code below is for testing
        # print(f"index after shifted of letter {letter} is {alphabet_index}")
    print(f"The encrypted text is {encrypted_text}")


# TODO-2: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decrypt_text = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        # the code below is for testing
        # print(f"index of letter {letter} is {letter_index}")

        # this is the index after shifting backward
        new_index = letter_index - shift

        # the code below is for testing
        # print(f"The new index is {new_index}")

        # check if the new index is greater than the length of the alphabet
        # -> to avoid List Index Out of Range error -> but in this case, it is -26

        if new_index < -len(alphabet):
            num = int(new_index / len(alphabet))
            new_index -= len(alphabet) * num

            # the code below is for testing
            # print(f"index after shifted of letter {letter} is {new_index}")

        decrypt_text += alphabet[new_index]

    print(f"The decrypted text is {decrypt_text}")


# TODO-3: Call the encrypt function and pass in the user inputs.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("you enter the wrong input")

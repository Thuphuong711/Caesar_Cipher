alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_of_program = False
while end_of_program == False :

  import art
  print(art.logo)

  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number:\n"))

  #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar() to make the code shorter

  def caesar(direction, start_text, shift):
    end_text = ""
    if direction == "decode":
      shift*= -1
    for char in text :
        # TODO-3: What happens if the user enters a number/symbol/space?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
      #this is to encode a paragraph, not just a single word
      if char not in alphabet:
        end_text += char
      else :
        letter_index = alphabet.index(char)
        # this is the index after shifting
        new_index = letter_index + shift
  
        # if ( new_index < -len(alphabet) ) or ( new_index >= len(alphabet) ) :
        #   num = int(new_index / len(alphabet))
        #   new_index -= len(alphabet) * num

        #Another simpler way to resolve the code when the shift is larger which can cause List index out of range error
        new_index = (letter_index + shift) % len(alphabet)
        
        end_text += alphabet[new_index]

    print(f"\nThe {direction} text is: {end_text}")

  
  #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
  caesar(direction, text, shift)

  restart = input("\nType Yes if you want to continue the program. Otherwise, type No :\n")
  if "no" == restart.lower():
    end_of_program = True
    print("\nThe program end. Good bye! ")
  else :
    print("\n\n")

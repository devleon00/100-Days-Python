from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasear(text, shift, direction):
    final_string = ""
    for letter in text:
        if letter in alphabet:
            if direction == "encode":
                encypt_index = alphabet.index(letter) + shift
                encrypt_letter = encypt_index % 26 if encypt_index > 25 else encypt_index
            
            elif direction == "decode":
                encypt_index = alphabet.index(letter) - shift
                encrypt_letter = encypt_index + 26 if encypt_index < 0 else encypt_index
        else:
            encrypt_letter = letter
        final_string += alphabet[encrypt_letter]
        
    print(f"The output is {final_string}")

restart = "yes"
while restart == "yes":
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasear(text, shift, direction)
    restart = input("You want to restart the cipher program? 'yes' or 'not'")
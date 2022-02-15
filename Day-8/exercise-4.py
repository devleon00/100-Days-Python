alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasear(text, shift):
    if direction == "encode":
        encrypt_string = ""
        for letter in text:
            encypt_index = alphabet.index(letter) + shift
            encrypt_letter = encypt_index - 26 if encypt_index > 25 else encypt_index
            encrypt_string += alphabet[encrypt_letter]
        print(f"The encoded text is {encrypt_string}")

    elif direction == "decode":
        decrypt_string = ""
        for letter in text:
            encypt_index = alphabet.index(letter) - shift
            encrypt_letter = encypt_index + 26 if encypt_index < 0 else encypt_index
            decrypt_string += alphabet[encrypt_letter]
        print(f"The decoded text is {decrypt_string}")
    else:
        print("Incorrect output")

ceasear(text, shift)
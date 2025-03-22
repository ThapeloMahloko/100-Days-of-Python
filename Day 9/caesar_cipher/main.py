from caesar_cipher import caesar_cipher
from art import logo

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    game_status = input("Do you want to continue Ciphering?[Yes/No]")
    caesar_cipher(direction, text, shift)
    if game_status.lower() == "no":
        print("Ciphering Complete")
        break
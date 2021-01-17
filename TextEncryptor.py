import tkinter
import os
#note that the following line makes this program user-specific i.e. "kroon" and is yet to be tested on Windows
desktop = os.path.expanduser("~/Desktop")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .!?/+-,'

print("Caeser Cipher-style Encryptor, by George Kroon |\n20/09/2019                                     |\n-----------------------------------------------")

enterKey = input('\nPlease enter a cipher shift-key (0-69): ')
key = int(enterKey)
cipherText = ''

message = input('\nPlease enter a message:\n')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        # print ("\nThis character was in position " + str(position))
        newPosition = (position + key) % 70
        # print ("\nIts new position is " + str(newPosition))
        newCharacter = alphabet[newPosition]
        # print("\nYour enciphered character is " + str(newCharacter))
        cipherText += newCharacter
    else:
        cipherText += character

print('\n\nYour ciphertext: "' + str(cipherText) + '"\n')

print("\nThis will now be saved to your desktop as a text file called 'CipherText'.\nBeware that any other file of that name in the same location will be overwitten.\nRemember, you may want to delete this file immediately after use for security purposes.")

CipherText = open(str(desktop)+"/CipherText.txt", "w+")

CipherText.write("Encrypted Text:\n")

CipherText.write(cipherText)

CipherText.close()

input("\n\nPress ENTER when you are ready to close this programme")


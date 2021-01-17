
import os
#note that the following line makes this program user-specific i.e. "George" and is yet to be tested on Windows
desktop = os.path.expanduser("~/Desktop")

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .!?/+-,'

print("Caeser Cipher-style Decryptor, by George Kroon |\n20/09/2019                                     |\n-----------------------------------------------")

enterKey = input('\nPlease enter the cipher shift-key used to encrypt the message: ')
key = int(enterKey)
if key<69 or key>0:
    print("\nValid key entered")
else:
    print("\nInvalid key entered")
    enterKey = input('\nPlease enter the cipher shift-key number used to encrypt the message: ')

message = ''

encryptedMessage = input('\nPlease enter the encrypted message below:\n')

for character in encryptedMessage:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + (70-key)) % 70
        newCharacter = alphabet[newPosition]
        message += newCharacter
    else:
        message += character

print('\n\nThe message reads: "' + str(message) + '"\n')

print("\nThis will now be saved to your desktop as a text file called 'DecipheredText'.\nBeware that any other file of that name in the same location will be overwitten.\nRemember, you may want to delete this after reading it for security purposes.")

DecipheredText = open(str(desktop)+"/DecipheredText.txt", "w+")

DecipheredText.write("Deciphered Text:\n")

DecipheredText.write(message)

DecipheredText.close()

input("\n\nPress ENTER when you're ready to close this programme")

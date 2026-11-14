
print("\n=========================================")
print("              CRYPTOVA")
print("       Your Words, Your Secret")
print("=========================================\n")
print("Welcome to CRYPTOVA!\n")

while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    print("1. Encode a Message")
    print("2. Decode a Message")
    print("3. Exit \n")

    x = int(input("Enter your choice: "))

    if x == 1:
        text = str(input("Type your message: "))

        while True:
            try:
                shift = int(input("Type the shift number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number. ")

        def encrypt(original_text, shift_amount):
            encoded_text = ""
            for letter in original_text:
                if letter.lower() in alphabet:
                    shifted_position = (alphabet.index(letter.lower()) + shift_amount) % 26

                    if letter.isupper():
                        encoded_text += alphabet[shifted_position].upper()
                    else:
                        encoded_text += alphabet[shifted_position]

                elif letter in number:
                    shifted_position = (number.index(letter) + shift_amount) % 10
                    encoded_text += number[shifted_position]
                else:
                    encoded_text += letter
            print(f"Here is the encoded message: {encoded_text}\n")
        encrypt(original_text=text, shift_amount=shift)

    if x == 2:
        text = str(input("Type your message: "))

        while True:
            try:
                shift = int(input("Type the shift number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number. ")

        def decrypt(original_text, shift_amount):
            decoded_text = ""
            for letter in original_text:
                if letter.lower() in alphabet:
                    shifted_position = (alphabet.index(letter.lower()) - shift_amount) % 26

                    if letter.isupper():
                        decoded_text += alphabet[shifted_position].upper()
                    else:
                        decoded_text += alphabet[shifted_position]

                elif letter in number:
                    shifted_position = (number.index(letter) - shift_amount) % 10
                    decoded_text += number[shifted_position]
                else:
                    decoded_text += letter
            print(f"Here is the decoded message: {decoded_text}\n")
        decrypt(original_text = text, shift_amount = shift)

    if x == 3:
        print("Thank you for using CRYPTOVA!")
        break

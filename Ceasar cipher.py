def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)

        else:
            encrypted_text += char 
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)

        else:
            decrypted_text += char 
    return decrypted_text

def get_valid_choice():
    while True:
        choice = input("Enter '1' to encrypt or '2' to decrypt: ").strip()
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def get_valid_key():
    while True:
        try:
            key = int(input("Enter the key (an integer):"))
            return key
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the encryption and decryption tool!")

    while True:
        choice = get_valid_choice()

        text = input("Enter the text:")
        key = get_valid_key()

        if choice == '1':
            result = encrypt(text, key)
            print("Encrypted text:", result)
        elif choice == '2':
            result = decrypt(text, key)
            print("Decrypted text:", result)

        again = input("Do you want to try again? (Y/N): ").lower()
        if again != 'y':
            print("Thank you for using the tool.")
            break

main()


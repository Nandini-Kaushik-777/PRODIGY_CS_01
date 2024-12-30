def encrypt(text, shift):
    """
    Encrypts the text using Caesar cipher with the given shift.
    """
    encrypted_text = ""

    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it as it is
            encrypted_text += char

    return encrypted_text

def decrypt(text, shift):
    """
    Decrypts the text using Caesar cipher with the given shift.
    """
    return encrypt(text, -shift)

def main():
    """
    Main function to run the Caesar cipher program.
    """
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (Enter 'q' to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()

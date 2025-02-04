def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

try:
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value (an integer): "))
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted message: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted message: {decrypted_text}")
except ValueError:
    print("Please enter a valid integer for the shift value.")

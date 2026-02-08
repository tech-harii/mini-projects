def vigenere(message, key, direction=1):
    key = key.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    result = []

    for char in message.lower():
        if not char.isalpha():
            result.append(char)
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.index(char)
            new_index = (index + offset * direction) % len(alphabet)
            result.append(alphabet[new_index])

    return ''.join(result)


def encrypt(message, key):
    return vigenere(message, key, 1)


def decrypt(message, key):
    return vigenere(message, key, -1)


print("=== Vigenere Cipher ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter an option (1/2): ")

if choice not in ('1', '2'):
    print("Invalid choice.")
else:
    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if choice == '1':
        result = encrypt(text, key)
        print("\nEncrypted text:", result)
    else:
        result = decrypt(text, key)
        print("\nDecrypted text:", result)
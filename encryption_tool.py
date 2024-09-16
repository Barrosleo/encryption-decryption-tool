# Implement the Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Implement the Vigenère Cipher
def vigenere_encrypt(text, key):
    key = key.upper()
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 65
            encrypted_text += chr((ord(char) - shift_amount + key_shift) % 26 + shift_amount)
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(text, key):
    key = key.upper()
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 65
            decrypted_text += chr((ord(char) - shift_amount - key_shift) % 26 + shift_amount)
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

# Test the Functions
if __name__ == "__main__":
    text = "Hello, World!"
    shift = 3
    key = "KEY"

    caesar_encrypted = caesar_encrypt(text, shift)
    caesar_decrypted = caesar_decrypt(caesar_encrypted, shift)
    print(f"Caesar Cipher:\nEncrypted: {caesar_encrypted}\nDecrypted: {caesar_decrypted}")

    vigenere_encrypted = vigenere_encrypt(text, key)
    vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, key)
    print(f"Vigenère Cipher:\nEncrypted: {vigenere_encrypted}\nDecrypted: {vigenere_decrypted}")

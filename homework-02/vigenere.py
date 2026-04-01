def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    key_len = len(keyword)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[key_index % key_len].lower()) - ord('a')

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    key_len = len(keyword)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[key_index % key_len].lower()) - ord('a')

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char

    return plaintext
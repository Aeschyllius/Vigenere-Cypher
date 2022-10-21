

def alphabetize_user_input(text):
    result = ''
    # Appends string if in english, then capitalizes it
    for i in text:
        if i.isalpha():
            result += i
    result = result.upper()
    return result


def main():
    # Asks the user for their desired text to be encrypted
    print('Please enter what you would like encrypted')
    plaintext = input()
    new_plaintext = alphabetize_user_input(plaintext)
    # Asks the user for their desired key
    print('Please enter a key')
    key = input()
    new_key = alphabetize_user_input(key)

    # Checks that the key isn't smaller than the plaintext
    # If the key is smaller, the key repeats until their length is the same
    if len(new_plaintext) != len(new_key):
        for i in range(len(new_plaintext) - len(new_key)):
            new_key += (new_key[i % len(new_key)])

    # Encrypts each letter using ord to find ascii value of characters
    encrypted_text = []
    for i in range(len(new_plaintext)):
        x = (ord(new_plaintext[i]) + ord(new_key[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    ciphertext = ("".join(encrypted_text))
    print(f"Your encrypted text is \n{ciphertext}")


main()

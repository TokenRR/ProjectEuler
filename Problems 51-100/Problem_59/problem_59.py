import time
import itertools
import string


def decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using the XOR encryption with the given key.

    Parameters:
    ciphertext (list of int): The ASCII codes of the encrypted message.
    key (str): The decryption key.

    Returns:
    str: The decrypted message.
    """
    return ''.join(chr(char ^ ord(key[i % len(key)])) for i, char in enumerate(ciphertext))


def find_key(ciphertext):
    """
    Find the key for the XOR encrypted ciphertext.

    Parameters:
    ciphertext (list of int): The ASCII codes of the encrypted message.

    Returns:
    str: The decryption key.
    """
    # Assuming the key is three lowercase letters
    for key in itertools.product(string.ascii_lowercase, repeat=3):
        key = ''.join(key)
        decrypted_text = decrypt(ciphertext, key)
        # Assuming the decrypted text must contain common English words
        if ' the ' in decrypted_text:
            return key
    return None


def read_cipher_file(file_path):
    """
    Read the cipher file and return the ASCII codes as a list of integers.

    Parameters:
    file_path (str): The path to the cipher file.

    Returns:
    list of int: The ASCII codes of the encrypted message.
    """
    with open(file_path, 'r') as file:
        return [int(num) for num in file.read().strip().split(',')]


def sum_of_ascii_values(message):
    """
    Calculate the sum of ASCII values of all characters in the message.

    Parameters:
    message (str): The decrypted message.

    Returns:
    int: The sum of ASCII values.
    """
    return sum(ord(char) for char in message)


if __name__ == "__main__":
    start_time = time.time()
    cipher_file_path = "Problem_59\\0059_cipher.txt"
    ciphertext = read_cipher_file(cipher_file_path)
    key = find_key(ciphertext)
    decrypted_message = decrypt(ciphertext, key)
    
    # print(f"\nDecrypted message: {decrypted_message}\n")
    print(f"Answer = {sum_of_ascii_values(decrypted_message)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    
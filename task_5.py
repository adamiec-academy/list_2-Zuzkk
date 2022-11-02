def cipher(text, shift):
    result = ""
    shift = shift % 26
    for letter in text:
        if letter == " ":
            result += letter
        elif letter.isupper() and ord(letter) + shift > ord('Z'):
            result += chr(ord(letter) + shift - 26)
        elif not letter.isupper() and ord(letter) + shift > ord('z'):
            result += chr(ord(letter) + shift - 26)
        else:
            result += chr(ord(letter) + shift)
    return print(result)


def decipher(text, shift):
    result = ""
    for letter in text:
        if letter == " ":
            result += letter
        elif letter.isupper() and ord(letter) - shift < ord('A'):
            result += chr(ord(letter) - shift + 26)
        elif not letter.isupper() and ord(letter) - shift < ord('a'):
            result += chr(ord(letter) - shift + 26)
        else:
            result += chr(ord(letter) - shift)
    return print(result)


cipher("Imperator", 1)
decipher("Jnqfsbups", 1)

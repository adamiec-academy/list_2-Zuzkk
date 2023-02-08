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
    return result


def decipher(text, shift):
    return cipher(text, -shift)

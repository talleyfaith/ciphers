def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount
    
    if unicode_value > 126:     
        new_letter = chr(unicode_value  -95)
    else:
        new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):
    result = ""

    for letter in message:
        unicode_value = ord(letter) + shift_amount
        if unicode_value - shift_amount < 32:
            result += shift(letter, -shift_amount + 95)
        else:
            result += shift(letter, -shift_amount)
        

    return result

unencrypted_message = "abcdwxyz"
encrypted_message = encrypt(unencrypted_message, 10)
decrypted_message = decrypt(encrypted_message, 10)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)



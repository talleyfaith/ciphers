alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRs StTuUvVwWxXyYzZ123456789!@#$%^&*()_+-=,./<>?;:'\"[]{}\\|~`" 
key = " plmkoijnbhuygvcftrdxsezawqQAZXWSEDCRFVGBTNYJHUMKILOP*&^%$#()-+1236,./<>?;:'\"[]{}\\|~`54789@!=_"

print(len(alphabet))
print(len(key))

def encrypt(message):
    result = ""

    for letter in message:
      loc = alphabet.find(letter)
      result += key[loc]

    return result

def decrypt(message):
    result = ""

    for letter in message:
      loc = key.find(letter)
      result += alphabet[loc]

    return result

unencrypted_message = "All around me are familiar faces / Worn out places, worn out faces / Bright and early for their daily races / Going nowhere, going nowhere"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

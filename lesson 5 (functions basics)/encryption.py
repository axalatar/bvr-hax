alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(message):
    letters = []
    for i, letter in enumerate(message):
        if letter in alphabet:
            letters.append(alphabet[(alphabet.index(letter) + 10 + i) % 26])
        else:
            letters.append(letter)
    return "".join(letters)

def decrypt(message):
    letters = []
    for i, letter in enumerate(message):
        if letter in alphabet:
            letters.append(alphabet[(alphabet.index(letter) - 10 - i) % 26])
        else:
            letters.append(letter)
    return "".join(letters)

encrypted = encrypt("hey man! what's up?")
print(encrypted) # rpk apd! pbvp'q uq?

decrypted = decrypt(encrypted)
print(decrypted) # hey man! what's up?
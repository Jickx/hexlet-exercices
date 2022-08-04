# encrypt("move") => 'omev'
# encrypt("attack") => 'taatkc'
# encrypt("go!") => 'og!'

def encrypt(word):
    encrypted_word = ''
    for i in range(0, len(word) - 1, 2):
        encrypted_word += word[i + 1]
        encrypted_word += word[i]
    return encrypted_word

print(encrypt('move'))
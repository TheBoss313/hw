from static.proj1.const import alph as alphabet, symb as symbols


def encrypt_atbash(text):
    letters = []
    for i in text.lower():
        if i in symbols:
            letters.append(i)
            continue
        letters.append(alphabet[len(alphabet) - alphabet.find(i) - 1])
    return ''.join(letters)

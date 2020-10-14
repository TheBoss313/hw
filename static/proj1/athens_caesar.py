from static.proj1.const import alph as alphabet, symb as symbols


def get_divisors_number(number):
    divisors_number = []
    divisors_number_result = []
    for i in range(2, number + 1):
        if number % i == 0:
            divisors_number.append(i)
            continue
        for j in divisors_number:
            if i % j == 0:
                divisors_number_result.append(i)
                
    for i in divisors_number:
        divisors_number_result.append(i)

    divisors_number_result.sort()
        
    return divisors_number_result


def inverse_element(element, mod):
    for number in range(1, mod):
        if number * element % mod == 1:
            return number
    return -1


def encrypt_athens_caesar(word, pos, key):
    divisors_number = get_divisors_number(len(alphabet))
    if key in divisors_number:
        return 'Недопустимый ключ. Используйте значение, \
не входящее в следующий список: ' + str(divisors_number)
    
    letters = []
    for i in word:
        if i in symbols:
            letters.append(i)
            continue
        letters.append(alphabet[(alphabet.find(i) * key + pos) % len(alphabet)])
    return ''.join(letters)


def decrypt_athens_caesar(word, pos, key):
    letters = []
    inversed_key = inverse_element(key, len(alphabet))
    for i in word:
        if i in symbols:
            letters.append(i)
            continue
        letters.append(alphabet[((alphabet.find(i) - pos) * inversed_key) % len(alphabet)])
    return ''.join(letters)

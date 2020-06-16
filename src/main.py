# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    password = ''
    numbers_list = list()
    letters_list = list(string.ascii_letters)
    for number in range(9):
        numbers_list.append(str(number))
    final_list = letters_list + numbers_list + SYMBOLS
    pass_length = random.randint(8,16)
    for i in range(pass_length):
        char = take_random_letter(final_list)
        password += char 
    return password
 


def take_random_letter(ascii_list):
    character = random.choice(ascii_list)
    return character


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()

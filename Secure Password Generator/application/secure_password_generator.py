from random import sample


def get_valid_amount_of_passwords():
    amount_of_passwords = input('Сколько паролей Вы хотите сгенерировать? Введите число.')
    while not (amount_of_passwords.isdigit() and int(amount_of_passwords) > 0):
        print('Введено неверное значение. Пожалуйста, введите число больше нуля')
        amount_of_passwords = input()
    return int(amount_of_passwords)

def get_valid_length_of_password():
    length_of_password = input('Какая длина будет у каждого пароля? Введите число.')
    while not (length_of_password.isdigit() and int(amount_of_passwords) > 0):
        print('Введено неверное значение. Пожалуйста, введите число больше нуля.')
        length_of_password = input()
    return int(length_of_password)


def get_valid_answer_digits():
    answer_digits = input(f'Включать ли цифры {digits}?').lower()
    while not (answer_digits == 'да' or answer_digits == 'нет'):
        print('Введено неверное значение. Пожалуйста, введите "да" или "нет".')
        answer_digits = input().lower()
    return answer_digits

def get_valid_answer_uppercase_letters():
    answer_uppercase_letters = input(f'Включать ли прописные буквы {uppercase_letters}?').lower()
    while not (answer_uppercase_letters == 'да' or answer_uppercase_letters == 'нет'):
        print('Введено неверное значение. Пожалуйста, введите "да" или "нет".')
        answer_uppercase_letters = input().lower()
    return answer_uppercase_letters 

def get_valid_answer_lowercase_letters():
    answer_lowercase_letters = input(f'Включать ли строчные буквы {lowercase_letters}?').lower()
    while not (answer_lowercase_letters == 'да' or answer_lowercase_letters == 'нет'):
        print('Введено неверное значение. Пожалуйста, введите "да" или "нет".')
        answer_lowercase_letters = input().lower()
    return answer_lowercase_letters 

def get_valid_answer_punctuation():
    answer_punctuation = input(f'Включать ли символы {punctuation}?').lower()
    while not (answer_punctuation == 'да' or answer_punctuation == 'нет'):
        print('Введено неверное значение. Пожалуйста, введите "да" или "нет".')
        answer_punctuation = input().lower()
    return answer_punctuation

def get_valid_answer_few_punctuation():
    answer_few_punctuation = input(f'Исключать ли неоднозначные символы "il1Lo0O"?').lower()
    while not (answer_few_punctuation == 'да' or answer_few_punctuation == 'нет'):
        print('Введено неверное значение. Пожалуйста, введите "да" или "нет".')
        answer_few_punctuation = input().lower()
    return answer_few_punctuation



def get_chars_collection():
    chars = ''
    if get_valid_answer_digits() == 'да':
        chars += digits
    if get_valid_answer_uppercase_letters() == 'да':
        chars += uppercase_letters
    if get_valid_answer_lowercase_letters() == 'да':
        chars += lowercase_letters
    if get_valid_answer_punctuation() == 'да':
        chars += punctuation
    if get_valid_answer_few_punctuation() == 'да':
        for c in('il1Lo0O'):
            chars.replace(c, '')
    return chars


def generate_password(chars, length):
        password_as_array = sample(chars, length)
        return ''.join(password_as_array)

def set_app_config():
    global digits
    digits = '0123456789'
    global lowercase_letters
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    global uppercase_letters
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    global punctuation
    punctuation = '!#$%&*+-=?@^_'


if __name__ == "__main__":
    set_app_config()

    print('Вы запустили генератор паролей. Пожалуйста, ответьте на вопросы ниже.')

    amount_of_passwords = get_valid_amount_of_passwords()
    length_of_password = get_valid_length_of_password()
    chars = get_chars_collection()
    if chars == '':
        print('Недостаточно символов для генерации паролей.')
    else:
        for _ in range(amount_of_passwords):
            new_password = generate_password(chars, length_of_password)
            print(new_password)
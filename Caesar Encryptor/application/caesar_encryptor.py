def en_de_crypt_char(direction, char, ROT, language):
    alphabet = get_alphabet_to_use(language, char.isupper())
    index_char = alphabet.find(char)
    if direction == 'ш':
        new_index_char = (index_char + ROT) % len(alphabet)
    if direction == 'д':
        new_index_char = (index_char - ROT) % len(alphabet)
    new_char = alphabet[new_index_char]
    return new_char


def create_new_string(text, direction, rotation, language):
    crypted_text = ''
    for c in text:
            crypted_text += en_de_crypt_char(direction, c, rotation, language)
    return crypted_text
    

def get_valid_direction():
    direction = input('Введите "ш", если хотите зашифровать текст, введите "д", если хотите дешифровать текст.').lower()
    while not (direction == 'д' or direction == 'ш'):
        print('Введено неверное значение.')
        direction = input('Введите "ш", если хотите зашифровать текст, введите "д", если хотите дешифровать текст.').lower()
    return direction


def get_valid_rotation():
    rotation = input('Укажите число - ключ к шифрованию/ дешифрованию.')
    while not rotation.isdigit():
        print('Введено неверное значение.')
        rotation = input('Укажите число - ключ к шифрованию/ дешифрованию.')
    return int(rotation)


def set_alphabet():
    global low_register_eng 
    low_register_eng = 'abcdefghijklmnopqrstuvwxyz'
    global upper_register_eng
    upper_register_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    global low_register_rus
    low_register_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    global upper_register_rus
    upper_register_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_language_to_use():
    language = input('Введите "рус", если хотите зашифровать/ дешифровать текст на русском языке, или введите "eng", если хотите зашифровать/ дешифровать текст на английском языке.').lower()
    while not (language == 'рус' or language == 'eng'):
        print('Введено неверное значение.')
        language = input('Введите "рус", если хотите зашифровать/ дешифровать текст на русском языке, или введите "eng", если хотите зашифровать/ дешифровать текст на английском языке.')
    return language


def get_alphabet_to_use(lang, upper):
    if lang == 'рус' and upper == True:
        return upper_register_rus
    if lang == 'рус' and upper == False:
        return low_register_rus
    if lang == 'eng' and upper == True:
        return upper_register_eng
    if lang == 'eng' and upper == False:
        return low_register_eng


def get_valid_text(language):
    is_valid = False
    while not is_valid:
        text = input('Введите текст для шифрования/ дешифрования.')
        the_same = True
        if language == 'рус':
            for c in text:
                if c in(low_register_eng) or c in(upper_register_eng):
                    print('В тексте содержатся английские буквы.  Введите текст на русском языке.')
                    the_same = False
                    break
        if language == 'eng':
            for c in text:
                if c in(low_register_rus) or c in(upper_register_rus):
                    print('В тексте содержатся русские буквы.  Введите текст на английском языке.')
                    the_same = False
                    break
        if the_same == True:
            is_valid = True
    return text


if __name__ == "__main__":
    set_alphabet()
    print('Добро пожаловать в программу по шифрованию/ дешифрованию текстов. Давайте начнем.')
    while True:
        direction = get_valid_direction()
        rotation = get_valid_rotation()
        language = get_language_to_use()
        text = get_valid_text(language)
        text_to_print = create_new_string(text, direction, rotation, language)

        print(text_to_print)

        question = input('Хотите еще раз? Введите "да" или "нет".')
        if question == 'нет':
            print('До встречи!')
            break
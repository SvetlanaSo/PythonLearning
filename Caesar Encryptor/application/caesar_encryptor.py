def encryption(symbol_before, ROT, quantity):
    encrypted_symbol = (symbol_before + ROT) % quantity
    return encrypted_symbol


def de_cryption(symbol_after, ROT, quantity):
    decrypted_symbol = (symbol_after - ROT) % quantity
    return decrypted_symbol


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


def set_alphabet_both_registers():
    global low_register_eng 
    low_register_eng = 'abcdefghijklmnopqrstuvwxyz'
    global upper_register_eng
    upper_register_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    global low_register_rus
    low_register_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    global upper_register_rus
    upper_register_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_alphabet_to_use():
    language = input('Введите "р", если хотите зашифровать/ дешифровать текст на русском языке, или введите "а", если хотите зашифровать/ дешифровать текст на английском языке.')
    while not (language == 'р' or language == 'а'):
        print('Введено неверное значение.')
        language = input('Введите "р", если хотите зашифровать/ дешифровать текст на русском языке, или введите "а", если хотите зашифровать/ дешифровать текст на английском языке.')
    return language

def get_valid_text(language):
    is_valid = False
    while not is_valid:
        text = input('Введите текст для шифрования/ дешифрования.')
        the_same = True
        if language == 'р':
            for c in text:
                if c in(low_register_eng) or c in(upper_register_eng):
                    print('В тексте содержатся английские буквы.  Введите текст на русском языке.')
                    the_same = False
                    break
        if language == 'а':
            for c in text:
                if c in(low_register_rus) or c in(upper_register_rus):
                    print('В тексте содержатся русские буквы.  Введите текст на английском языке.')
                    the_same = False
                    break
        if the_same == True:
            is_valid = True
    return text


if __name__ == "__main__":
    set_alphabet_both_registers()
    print('Добро пожаловать в программу по шифрованию/ дешифрованию текстов. Давайте начнем.')
    while True:
        direction = get_valid_direction()
        rotation = get_valid_rotation()
        language = get_alphabet_to_use()
        text = get_valid_text(language)




        #if direction == 'ш':
            #for c in text:
             #   if c.isalpha():
              #      text.replace(c, encryption(c, rotation, quantity))

      #  if direction == 'д':


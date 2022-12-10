

def encryption(symbol_before, ROT, quantity):
    encrypted_symbol = (symbol_before + ROT) % quantity


def de_cryption(symbol_after, ROT, quantity):
    decrypted_symbol = (symbol_after - ROT) % quantity



def set_alphabet_both_registers():
    low_register_eng = 'abcdefghijklmnopqrstuvwxyz'
    upper_register_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_register_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    upper_register_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


if __name__ == "__main__":
    print('Добро пожаловать в программу по шифрованию/ дешифрованию текстов. Давайте начнем.')
    while True:
        direction = input('Введите "ш", если хотите зашифровать текст, введите "д", если хотите дешифровать текст.').lower()
        if not (direction == 'д' or direction == 'ш'):
            print('Введено неверное значение.')
            continue
        else:
            


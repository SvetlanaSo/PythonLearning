import random as rd


def is_valid(number):
    for c in str(number):
        if not c in('0123456789'):
            return False
    if number == '':
        return False
    if not int(number) in range(1, 101):
        return False
    return True


if __name__ == "__main__":
    secret_num = rd.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')
    print('Мы загадали целое число от 1 до 100. Попробуете угадать? Введите число.')

    number_is_guessed = False
    while not number_is_guessed:
        checking_num = input()
        if not is_valid(checking_num):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        checking_num = int(checking_num)
        if checking_num == secret_num:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        if checking_num > secret_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if checking_num < secret_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
    



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

def play_guesser(secret_num):
    print('Добро пожаловать в числовую угадайку')
    print('Мы загадали целое число от 1 до 100. Попробуете угадать? Введите число.')

    number_is_guessed = False
    amount_of_attempts = 0
    while not number_is_guessed:
        amount_of_attempts += 1
        checking_num = input()
        if not is_valid(checking_num):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        checking_num = int(checking_num)
        if checking_num == secret_num:
            print('Вы угадали число, поздравляем!')
            print('Номер попытки, с которой угадано число:', amount_of_attempts)
            print('Спасибо, что играли в числовую угадайку.')
            number_is_guessed = True
        if checking_num > secret_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if checking_num < secret_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')

def want_to_play_again():
    print()
    print('Хотите сыграть еще раз? Введите "да" или "нет".')
    is_answer_correct = False
    while not is_answer_correct:
        answer = input().lower()
        if answer== 'да':
            return True
        if answer == 'нет':
            print('Еще увидимся...')
            return False
        else:
            print('Введено неверное значение. Введите "да" или "нет".')
        

if __name__ == "__main__":
    
    want_to_play_a_game = True
    while want_to_play_a_game:
        secret_num = rd.randint(1, 100)
        play_guesser(secret_num)
        if not want_to_play_again():
            want_to_play_a_game = False
            
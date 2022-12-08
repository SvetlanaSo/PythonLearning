import random as rd

def get_valid_number(maximum_value = "not defined"):
    number_to_check = input()
    while not is_valid(number_to_check, maximum_value):
        if maximum_value == "not defined":
            print(f'А может быть все-таки введем целое число больше 0?')
        else:
            print(f'А может быть все-таки введем целое число от 1 до {maximum_value}?')
        number_to_check = input()
    return int(number_to_check)

def is_valid(number, max_value = "not defined"):
    for c in str(number):
        if not c in('0123456789'):
            return False
    if number == '':
        return False
    if int(number) <= 0:
        return False
    if max_value != "not defined" and int(number) > max_value:
        return False

    return True

def play_guesser():
    print('Добро пожаловать в числовую угадайку')
    print('Введите верхнюю границу угадываемого числа.')
    upper_guessing_boundary = get_valid_number()
    secret_num = rd.randint(1, upper_guessing_boundary)
    print(f'Мы загадали целое число от 1 до {upper_guessing_boundary}. Попробуете угадать? Введите число.')

    number_is_guessed = False
    amount_of_attempts = 0
    while not number_is_guessed:
        amount_of_attempts += 1
        checking_num = get_valid_number(upper_guessing_boundary)
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
        play_guesser()
        if not want_to_play_again():
            want_to_play_a_game = False
            
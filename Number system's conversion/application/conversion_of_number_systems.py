def set_values():
    global all_values
    all_values = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_valid_answer():
    answer = input().lower()
    while not answer == 'да' and not answer == 'нет':
        print('Неверное значение. Введите "да" или "нет".')
        answer = input().lower()
    return answer


def get_valid_num_of_system():
    num = input()
    while not (num.isdigit() and 1 < int(num) < 37):
        print('Введено неверное значение. Введите число от 2 до 36 (включительно).')
        num = input()
    return int(num)


def get_valid_number(initial_system):
    number_is_invalid = True
    while number_is_invalid:
        number_is_invalid = False
        num = input().upper()
        for char in num:
            if char not in all_values[:initial_system]:
                number_is_invalid = True
                print('Введено неверное значение. Попробуйте снова.')
                break
    return num


def covert_into_10(initial_num, initial_system):
    initial_num = initial_num[::-1]
    converted_num = 0
    current_multiplier = 1
    for string_digit in initial_num:
        digit = all_values.find(string_digit)
        converted_num += digit * current_multiplier
        current_multiplier *= initial_system
    return int(converted_num)


def convert_into_required_system(number_to_convert, required_system):
    base = required_system
    numerator = number_to_convert
    quotient = numerator
    array_for_remainders = []
    while quotient > base:
        quotient = numerator // base
        remainder = numerator % base
        array_for_remainders.append(all_values[remainder])
        numerator = quotient
    if quotient > 9:
        quotient = all_values[quotient]
    array_for_remainders.reverse()
    
    converted_string = str(quotient) + ''.join(array_for_remainders)
    return converted_string


if __name__ == "__main__":
    print('Добро пожаловать в программу по переводу чисел из одной системы счисления в другую.')
    set_values()
    while True:
        print('Из какой системы счисления вы хотите осуществить перевод? Укажите число, соответствующее системе счисления.')
        print('Например, укажите "10", если хотите осуществить перевод из десятичной системы счисления, или "2" - если из двоичной системы счисления. Минимум - "2", максимум - "36".')
        initial_system = get_valid_num_of_system()
        print('Теперь укажите систему счисления, в которую хотите перевести число. Необходимо указать именно число, например "8". Минимум - "2", максимум - "36".') 
        required_system = get_valid_num_of_system()
        print('А теперь введите само число, которое хотите перевести.')
        number = get_valid_number(initial_system)
        converted_to_10_num = covert_into_10(number, initial_system)
        converted_to_required_sys_num = convert_into_required_system(converted_to_10_num, required_system)
        print(converted_to_required_sys_num)
        print()
        print('Хотите перевести еще какое-нибудь число? Введите "да" или "нет".')
        answer = get_valid_answer()
        if answer == 'нет':
            print('Программа завершена.')
            break

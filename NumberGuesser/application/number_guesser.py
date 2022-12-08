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



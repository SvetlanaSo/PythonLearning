import dictionary
import hangman

def get_valid_version():
    word_or_char = input('Введите букву или слово для проверки.').upper()
    while not word_or_char.isalpha():
        word_or_char = input('Недопустимое значение. Введите букву или слово.').upper()
    return word_or_char


def get_valid_answer():
    answer = input().lower()
    while not (answer == 'да' or answer == 'нет'):
        print('Введено некорректное значение. Введите "да" или "нет".')
        answer = input().lower()
    return answer


def play(word):

    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(hangman.display_hangman(tries), f'Количество доступных попыток: {tries}.', sep='\n')
    print(word_completion)
    while not guessed and tries > 0:
        version = get_valid_version()
        if version in guessed_letters or version in guessed_words:
            print('Вы уже вводили эту букву/ слово. Попробуйте еще раз.')
            continue
        
        if len(version) == 1:
            for i in range(len(word)):
                if word[i] == version:
                    word_completion = word_completion[:i] + version + word_completion[i + 1:]

            if word_completion == word:
                guessed = True
            guessed_letters.append(version)
        else:
            if version == word:
                guessed = True
            
            guessed_words.append(version)
    
        if version not in word:   
            tries -= 1

        if guessed:
            print(word_completion)
            print('Поздравляем, вы угадали слово! Вы победили!')
        elif tries == 0:
            print(hangman.display_hangman(tries))
            print(f'Вы не угадали слово за отведенное количество попыток. Загаданное слово: {word}.')
        else:
            print(hangman.display_hangman(tries), f'Количество доступных попыток: {tries}.', sep='\n')
            print(word_completion)

        


if __name__ == '__main__':
    while True:
        word_to_guess = dictionary.get_random_word()
        play(word_to_guess)
        print('Хотите сыграть еще раз? Введите "да" или "нет".')
        if get_valid_answer() == 'нет':
            break
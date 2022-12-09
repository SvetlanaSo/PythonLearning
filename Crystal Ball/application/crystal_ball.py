import random

def get_valid_yes_or_no_answer():
    answer_is_valid = False
    while not answer_is_valid:
        answer = input().lower()
        if answer == 'да' or answer == 'нет' or answer == 'yes' or answer == 'no':
            answer_is_valid = True
            return answer
        print('Это "да" или "нет"? Хочешь задать мне еще вопрос?')


if __name__ == "__main__":
    answers = ['Бесспорно',	'Мне кажется - да',	'Пока неясно, попробуй снова',	'Даже не думай', 'Предрешено',	'Вероятнее всего',	'Спроси позже',	'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',	'Лучше не рассказывать',	'По моим данным - нет', 'Определённо да',	'Знаки говорят - да',	'Сейчас нельзя предсказать',	'Перспективы не очень хорошие', 'Можешь быть уверен в этом',	'Да',	'Сконцентрируйся и спроси опять',	'Весьма сомнительно']
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как тебя зовут?')
    print(f'Привет, {name}!')

    while True:
        question = input('Задай мне вопрос.')
        print(random.choice(answers))
        print('Хочешь узнать ответ на еще какой-нибудь вопрос? Ответь: "да" или "нет".')
        answer = get_valid_yes_or_no_answer()
        if answer == 'нет' or answer == 'no':
            print('Возвращайся если возникнут вопросы!')
            break
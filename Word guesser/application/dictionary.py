from random import choice
word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз',
'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом']

def get_random_word():
    random_word = choice(word_list).upper()
    return random_word
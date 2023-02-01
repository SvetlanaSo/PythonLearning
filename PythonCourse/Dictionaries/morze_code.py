letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
    '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', 
    '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', 
    '....-', '.....', '-....', '--...', '---..', '----.'
    ]
dict_morse_code = dict(zip(letters, morse))

for el in input().upper():
    for key, value in dict_morse_code.items():
        if el == key:
            print(value, end=' ')
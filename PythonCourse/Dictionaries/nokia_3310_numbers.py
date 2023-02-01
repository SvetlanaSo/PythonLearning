buttons = {'.,?!:': '1', 'ABC': '2', 'DEF': '3', 'GHI': '4', 'JKL': '5', 
    'MNO': '6', 'PQRS': '7', 'TUV': '8', 'WXYZ': '9', ' ': '0'
    }

text = input().upper()
for el in text:
    for key, value in buttons.items():
        if el in key:
            pos = key.find(el)
            print(value * (pos + 1), end='')
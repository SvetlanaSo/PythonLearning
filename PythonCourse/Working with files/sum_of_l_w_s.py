with open('PythonCourse/Working with files/file.txt', encoding='utf-8') as f:
    lst = [line.rstrip() for line in f.readlines()]
    lines_num, words_num, letters_num = len(lst), 0, 0
    for line in lst:
        line_list = line.split()
        words_num += len(line_list)
        for word in line_list:
            for el in word:
                if el.isalpha():
                    letters_num += 1
print('Input file contains:', f'{letters_num} letters', f'{words_num} words', f'{lines_num} lines', sep='\n')
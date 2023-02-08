def get_dict(amount_of_countries):
    dict_ry = {}
    for _ in range(amount_of_countries):
        country, *cities = input().split()
        tmp_dict = dict.fromkeys(cities, country)
        dict_ry.update(tmp_dict)
    return dict_ry

def display_answer(dictionary, amount_of_cities):
    for _ in range(amount_of_cities):
        key = input()
        if key in dictionary:
            print(dictionary[key])

dictionary = get_dict(int(input()))
display_answer(dictionary, int(input()))
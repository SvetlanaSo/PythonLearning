def get_dict(amount_of_pairs):
    dict_of_syn = {}
    for _ in range(amount_of_pairs):
        word1, word2 = input().split()
        dict_of_syn[word1], dict_of_syn[word2] = word2, word1
    return dict_of_syn

dict_of_syn = get_dict(int(input()))
print(dict_of_syn[input()])
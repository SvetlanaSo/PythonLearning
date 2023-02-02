words = [word.strip('.,!?:;-, ') for word in input().lower().split()]
result = {}
for word in words:
    result[word] = result.get(word, 0) + 1

min_value, min_key = len(words), max(result)

for key, value in result.items():
    if value < min_value:
        min_value, min_key = value, key
    if value == min_value and key <=min_key:
        min_value, min_key = value, key

print(min_key)
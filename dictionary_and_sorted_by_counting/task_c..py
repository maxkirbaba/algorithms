from sys import stdin


def most_common_word(text):
    s = text.split()
    count_words = {}
    for word in s:
        count_words[word] = count_words.get(word, 0) + 1

    max_value = 0
    min_key = max(count_words.keys())
    for key, value in count_words.items():
        if value > max_value:
            max_value = value
            min_key = key
        elif value == max_value:
            min_key = min(key, min_key)
    return min_key


t = stdin.read()
print(most_common_word(t))

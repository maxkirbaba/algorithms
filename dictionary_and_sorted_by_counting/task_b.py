from sys import stdin


def count_of_element(text):
    s = text.split()
    count_words = dict()
    ans = []
    for word in s:
        count_words[word] = count_words.get(word, 0) + 1
        ans.append(str(count_words[word] - 1))
    return " ".join(ans)


t = stdin.read()

print(count_of_element(t))

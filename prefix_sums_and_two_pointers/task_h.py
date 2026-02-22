n, k = map(int, input().split())
string = input()

count_symbols = dict()
right = 0
final_len = 0
final_left = 0
count_symbols[string[0]] = 1

for left in range(len(string)):
    while right < (len(string)) and count_symbols[string[right]] <= k:
        right += 1
        if right < len(string):
            count_symbols[string[right]] = count_symbols.get(string[right], 0) + 1

    if final_len < (right - left):
        final_len = right - left
        final_left = left + 1

    count_symbols[string[left]] -= 1

print(final_len, final_left)

all_languages = set()
common_language = None
n = int(input())
for _ in range(n):
    m = int(input())
    languages = {input().strip() for _ in range(m)}
    if common_language is None:
        common_language = languages
    else:
        common_language &= languages
    all_languages |= languages

print(len(common_language))
for i in common_language:
    print(i)

print(len(all_languages))
for j in all_languages:
    print(j)

        


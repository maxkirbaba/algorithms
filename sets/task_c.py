n, m = map(int, input().split())

colors_a = set(int(input()) for i in range(n))
colors_b = set(int(input()) for i in range(m))

same_colors = sorted(colors_a & colors_b)
unique_col_a = sorted(colors_a - colors_b)
unique_col_b = sorted(colors_b - colors_a)

print(len(same_colors))
print(*same_colors)
print(len(unique_col_a))
print(*unique_col_a)
print(len(unique_col_b))
print(*unique_col_b)
new_number = input().replace("-", "").replace("(", "").replace(")", "")
if len(new_number) == 7:
    new_number = "495" + new_number

for i in range(3):
    number = input().replace("-", "").replace("(", "").replace(")", "")
    if len(number) == 7:
        number = "495" + number
    if new_number[-10:] == number[-10:]:
        print("YES")
    else:
        print("NO")
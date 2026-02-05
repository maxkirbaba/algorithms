from sys import stdin


def definition_of_the_type(a):
    cur_seq_type = 0
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            if cur_seq_type == 0:
                cur_seq_type = "ASCENDING"
            elif cur_seq_type == "CONSTANT":
                cur_seq_type = "WEAKLY ASCENDING"
            elif cur_seq_type == "DESCENDING" or cur_seq_type == "WEAKLY DESCENDING":
                cur_seq_type = "RANDOM"

        elif a[i] < a[i - 1]:
            if cur_seq_type == 0:
                cur_seq_type = "DESCENDING"
            elif cur_seq_type == "CONSTANT":
                cur_seq_type = "WEAKLY DESCENDING"
            elif cur_seq_type == "ASCENDING" or cur_seq_type == "WEAKLY ASCENDING":
                cur_seq_type = "RANDOM"

        elif a[i] == a[i - 1]:
            if cur_seq_type == 0:
                cur_seq_type = "CONSTANT"
            elif cur_seq_type == "ASCENDING":
                cur_seq_type = "WEAKLY ASCENDING"
            elif cur_seq_type == "DESCENDING":
                cur_seq_type = "WEAKLY DESCENDING"

        if cur_seq_type == "RANDOM":
            return cur_seq_type

    return cur_seq_type


seq = []
for line in stdin:
    n = int(line)
    if n == -2 * 10**9:
        break
    else:
        seq.append(n)


print(definition_of_the_type(seq))

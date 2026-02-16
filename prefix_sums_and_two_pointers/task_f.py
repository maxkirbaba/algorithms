number_of_classes = int(input())
capacity_of_airconditioners = list(map(int, input().split()))
number_of_models = int(input())

inf = 10**4
min_price = [inf] * (1001)

for j in range(number_of_models):
    power, cost = map(int, input().split())
    if cost < min_price[power]:
        min_price[power] = cost

for p in range(999, 0, -1):
    min_price[p] = min(min_price[p], min_price[p + 1])

total_cost = 0
for i in capacity_of_airconditioners:
    total_cost += min_price[i]

print(total_cost)

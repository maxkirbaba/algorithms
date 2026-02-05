from sys import stdin


bank_accounts = dict()


def dep(name, s):
    bank_accounts[name] = bank_accounts.get(name, 0) + s


def withdraw(name, s):
    bank_accounts[name] = bank_accounts.get(name, 0) - s


def balance(name):
    if name in bank_accounts:
        print(bank_accounts[name])
    else:
        print("ERROR")


def transfer(name1, name2, s):
    bank_accounts[name1] = bank_accounts.get(name1, 0) - s
    bank_accounts[name2] = bank_accounts.get(name2, 0) + s


def income(p):
    for name, s in bank_accounts.items():
        if s > 0:
            bank_accounts[name] += int((s / 100) * p)


for line in stdin:
    i = line.split()
    n = len(i)
    if n == 2:
        if i[0] == "BALANCE":
            balance(i[1])
        else:
            income(int(i[1]))
    elif n == 3:
        if i[0] == "DEPOSIT":
            dep(i[1], int(i[2]))
        elif i[0] == "WITHDRAW":
            withdraw(i[1], int(i[2]))
    elif n == 4:
        transfer(i[1], i[2], int(i[3]))

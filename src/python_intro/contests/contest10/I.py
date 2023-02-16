from sys import stdin

def deposit(name, s):
    if name in bank:
        bank[name] += s
    else:
        bank[name] = s

def withdraw(name, s):
    if name in bank:
        bank[name] -= s
    else:
        bank[name] = -s

def balance(name):
    if name not in bank:
        print('ERROR')
    else:
        print(bank[name])

def income(percent):
    for key, value in bank.items():
        if value > 0:
            bank[key] = int(value * ((int(percent) / 100) + 1))

bank = dict()
for line in stdin:
    line = line.strip()
    if line == "":
        break

    line = line.split()
    if line[0] == "BALANCE":
        balance(line[1])
    elif line[0] == "DEPOSIT":
        deposit(line[1], int(line[2]))
    elif line[0] == "WITHDRAW":
        withdraw(line[1], int(line[2]))
    elif line[0] == "INCOME":
        income(line[1])
    else:
        withdraw(line[1], int(line[3]))
        deposit(line[2], int(line[3]))
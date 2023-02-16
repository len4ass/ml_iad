import re
from collections import deque

# Замена not ... bad на good
def sub_task_1():
    s = input()

    results = re.findall("not.*bad", s)
    for result in results:
        s = s.replace(result, "good")

    return s

# Сумма чисел в строке
def sub_task_2():
    s = input()
    temporary_str = "0"
    result = 0

    for char in s:
        if char.isdigit():
            temporary_str += char
        else:
            result += int(temporary_str)
            temporary_str = "0"

    return result + int(temporary_str)

# Проверка эквивалентности с точностью до прокрутки
def sub_task_3():
    s1 = input()
    s2 = input()

    d = deque(s1)
    strings = []
    for i in range(0, len(d)):
        d.rotate(i)
        chars = list(d)
        s = ""

        for c in chars:
            s += c

        strings += [s]

    return s2 in strings

# Реверснуть слова в строке
def sub_task_4():
    s = input()
    l = s.split()[::-1]

    s = ""
    for i in range(0, len(l)):
        if i == len(l) - 1:
            s += l[i]
        else:
            s += l[i] + " "

    return s

if __name__ == '__main__':
    print(sub_task_1())
    print(sub_task_2())
    print(sub_task_3())
    print(sub_task_4())


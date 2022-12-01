# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
n = int(input('Введите длину списка: '))
list = []


def createlist(_n, _list):
    for i in range(_n):
        _list.append(randint(0, 10))
    print(_list)


def createnewlist(_n, _list):
    newlist = []
    for i in range(_n):
        if i <= _n - 1 - i:
            newlist.append(_list[i] + _list[_n - 1 - i])
    print(newlist)


createlist(n, list)
createnewlist(n, list)

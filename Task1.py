# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
from random import randint

n = int(input('Введите длину списка: '))
list = []


def createlist(_n, _list):
    for i in range(_n):
        _list.append(randint(0, 10))


def sum(_n, _list):
    sum = 0
    for i in range(1, n, 2):
        sum += _list[i]
    print(_list, 'Сумма элементов с нечетными индексами =', sum)


createlist(n, list)
sum(n, list)

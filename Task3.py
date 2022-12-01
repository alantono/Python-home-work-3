# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:  - [1.1, 1.2, 3.1, 10.01] => 0.19
import random
n = int(input('Введите длину списка: '))
list = []
for i in range(n):
    list.append(round(random.uniform(0, 10), 3))
    list[i] = round((list[i] - int(list[i])), 3)


def minmax(_list):
    min = _list[0]
    max = _list[0]
    for i in range(len(_list)):
        if min > _list[i]:
            min = _list[i]
        if max < _list[i]:
            max = _list[i]
    return max - min


print(list, ' =>', round((minmax(list)), 3))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите значеня для списка Фибоначчи: '))
list = [0, 1]
list1 = []

for i in range(n - 1):
    list.append(list[i + 1] + list[i])

for i in range(n):
    list1.append(list[-i - 1])

for i in range(0, n - 1, 2):
    list1[i] = list1[i] * -1

print(list1 + list)

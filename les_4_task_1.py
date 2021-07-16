'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

import random
import timeit

x = [random.randint(0, 100) for _ in range(0, 10)]
print(x)

def version1():
    min1 = 0
    min2 = 0

    for i, e in enumerate(x):
        if i == 0:
            min1 = e
        elif e <= min1:
            min2 = min1
            min1 = e
        elif e <= min2 or min2 == 0:
            min2 = e
    return min1, min2

def version2():
    min1_2 = 0
    min2_2 = 0
    for i, e in enumerate(x):
        if i == 0:
            min1_2 = e
        elif e < min1_2:
            min2_2 = min1_2
            min1_2 = e
        elif e == min1_2:
            min2_2 = e
    return min1_2, min2_2

def version3():
    y = sorted(x)
    return y[0], y[1]

print(timeit.timeit('version1()', setup='from __main__ import version1', number=1000000))
print(timeit.timeit('version2()', setup='from __main__ import version2', number=1000000))
print(timeit.timeit('version3()', setup='from __main__ import version3', number=1000000))

# version1 N = 1000000 result = 0.8284084
# version1 N = 1000000 result = 0.7385391000000001
# version1 N = 1000000 result = 0.306033

print("Вариант с испльзованием функции sorted является лучшим, т.к. он самый быстрый")

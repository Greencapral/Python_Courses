'''
Навыки: Целые числа, строки, арифметические операции, циклы

Вычисление среднего арифметического — одна из базовых задач в математике и программировании. Задача состоит в том, чтобы правильно обработать ввод данных и правильно округлить результат в большую сторону.

🎯 Условие:

Напиши функцию arithmetical_mean(a), которая принимает целые числа, введенные пользователем через пробел. Программа должна вычислить среднее арифметическое этих чисел и вывести результат как целое число, округленное в большую сторону.

Пример:

10 20 30 40 -> 25
100 200 100 -> 134
 -100 200 500 -> 200

'''

from math import ceil

def arithmetical_mean(a) ->int:
    nums = list(map(int,a.split()))
    sum = 0
    for i in range(len(nums)):
        sum+=nums[i]
    return ceil(sum / len(nums))

test1 = '10 20 30 40'
test2 = '100 200 100'
test3 = '-100 200 500'
test5 = ''

test5 = input('?')
print(test5)
print(type(test5))
print(arithmetical_mean(test5))

# arithmetical_mean(test1)
# arithmetical_mean(test2)
# arithmetical_mean(test3)
print(arithmetical_mean("1 2 3 4 5"))        # Ожидается: 3
print(arithmetical_mean("1 2 2"))

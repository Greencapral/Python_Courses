"""

Навыки: Функции, списки, словари, строки, циклы, ветвление

Визуализация данных — ключевой инструмент в аналитике. Даже простой текст можно представить в наглядной форме. В этой задаче тебе предстоит реализовать вертикальную гистограмму, отражающую частоту появления символов в строке.

🎯 Условие:

Напиши функцию histogram(data: str) -> str, которая принимает одну строку и возвращает строковое представление гистограммы, где каждый столбец показывает количество вхождений соответствующей буквы. Столбцы выравниваются по вертикали, а буквы располагаются внизу — по алфавиту.

Пример:

# input_data: ececceaebdadaeae
#     |
#     |
# |   |
# | | |
# | |||
# |||||
# abcde

"""


def histogram(data: str) -> str:
    result = ''
    str_dif = {}
    podpisi = ''

    for char in data:                    # цикл для сбора различных букв и их подсчета
        if char not in str_dif:
            str_dif[char] = 1
        else:
            str_dif[char] += 1

    peak = max(str_dif.values())         # запоминаем максимальный пик
    str_dif = sorted(str_dif.items())    # сортируем буковки
    n = len(str_dif)                     # понимаем ширину графика

    for i in range(peak, 0, -1):         # цикл по высоте пика
        for j in range(n):               # цикл по ширине
            if int(str_dif[j][1]) < i:   # если по ключу значение меньше номера ряда то "пробел"
                result = result + ' '
            else:
                result = result + '|'    # иначе "палка"
        result = result + '\n'           # не забываем переводить строку
        # peak-=1

    for x in str_dif:                    # наковыриваем буковок отдельно, для подписи
        podpisi = podpisi + x[0]
    result = result + t2

    return result


test = 'ececceaebdadaeae'
test2 = 'dbcaabdc'
test3 = 'aaabbc'
test4 = 'a b a!b'
test5 = 'abcde'
test6 = 'aaaaaa'

t1 = histogram(test)
t2 = histogram(test2)
t3 = histogram(test3)
t4 = histogram(test4)
t5 = histogram(test5)
t6 = histogram(test6)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)

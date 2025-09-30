'''

Навыки: функции, строки, циклы, ветвления

В некоторых задачах по информационной безопасности и обработке текстов используется простой, но показательный алгоритм — шифр Цезаря. Это классический метод подстановки, в котором каждая буква заменяется другой с фиксированным смещением по алфавиту. Твоя задача — реализовать функцию, которая производит такое шифрование.

🎯 Условие:

Напиши функцию caesar_cipher(data: str, key: int) -> str, которая принимает:

data: исходную строку;

key: целое число — смещение по алфавиту.

Результат — новая строка, в которой каждая буква заменена на соответствующую, сдвинутую на key позиций.

Все символы, не являющиеся буквами (пробелы, знаки препинания, цифры и пр.), остаются без изменений.

Пример:

Doggy, 5 -> ItllD
Python is the BEST!, 20 -> jSNBIH CM NBy VYmn!

'''


from string import ascii_letters as alpha

def caesar_cipher(data: str, key: int) -> str:
    # print(data)
    return ''.join(map(
                        (lambda bukva: ((alpha[alpha.find(bukva) + key])
                                        if (alpha.find(bukva) + key) < len(alpha)
                                          else alpha[alpha.find(bukva) + key - len(alpha)])
                                            if bukva in alpha else bukva), data))
# test = 'Doggy'
# key = 5
#
# test2 ='abcXYZ'
# key2 = 3
#
# print(alpha)
# print(caesar_cipher(test, key))
# print(caesar_cipher(test2, key2))

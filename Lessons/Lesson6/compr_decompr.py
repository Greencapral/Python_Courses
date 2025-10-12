'''
🎯 Условие:

Реализуйте класс RLE, который содержит два метода:

rle_compression(data: str) -> str — принимает строку и возвращает её сжатую версию по алгоритму RLE, где повторяющиеся символы заменяются на один символ и количество его повторений.

rle_uncompression(compression_data: str) -> str — принимает строку, полученную в результате RLE-сжатия (например, 'a3b2'), и возвращает исходную строку, воссоздавая повторяющиеся символы.

ℹ️ Примечания

На вход подаются только корректно сформированные строки.

В сжатой строке каждый символ сопровождается одной цифрой — количеством повторений.

Все символы — латинские буквы, регистр имеет значение.

Для сжатия можно использовать как простой цикл, так и функцию groupby из модуля itertools.

Примеры использования

amateur_compressed = RLEAmateur.rle_compression('abbcccaabbbc')
print(amateur_compressed)  # Вывод: a1b2c3a2b3c1

amateur_uncompressed = RLEAmateur.rle_uncompression('a1b2c3a2b3c1')
print(amateur_uncompressed)  # Вывод: abbcccaabbbc

'''


# from itertools import groupby

class RLE:
    @staticmethod
    def rle_compression(data: str) -> str:
        """Сжимает строку с использованием RLE"""
        stroka_scheta = []
        str_dif = []
        res = ''
        i = 1
        counter = 1

        while i < len(data):
            if data[i - 1] == data[i]:
                counter += 1
            else:
                str_dif.append(data[i - 1])
                stroka_scheta.append(counter)
                counter = 1
            i += 1
        str_dif.append(data[-1])
        stroka_scheta.append(counter)

        i = 0
        while i < len(str_dif):
            res = res + str_dif[i] + str(stroka_scheta[i])
            i += 1

        return res

    @staticmethod
    def rle_uncompression(compression_data: str) -> str:
        """Восстанавливает строку из сжатого представления RLE."""
        i = 0
        res = ''

        while i < len(compression_data):
            j = 0
            while j < int(compression_data[i + 1]):
                res = res + compression_data[i]
                j += 1
            i += 2

        return res


RLEAmateur = RLE()

amateur_compressed = RLEAmateur.rle_compression('abbcccaabbbc')
print(amateur_compressed)

amateur_uncompressed = RLEAmateur.rle_uncompression('a1b2c3a2b3c1')
print(amateur_uncompressed)

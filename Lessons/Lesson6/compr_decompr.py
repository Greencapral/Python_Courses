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
from itertools import groupby

class RLE:
   @staticmethod
   def rle_compression(data: str) -> str:
       s = groupby(data)
       for i,j in s:
        print(i,j) # AAAAAAAAA!!!!!!
       return ''.join(str(s) for s in groupby(data))
       """Сжимает строку с использованием RLE"""

   @staticmethod
   def rle_uncompression(compression_data: str) -> str:
       """Восстанавливает строку из сжатого представления RLE."""

RLEAmateur= RLE()

amateur_compressed = RLEAmateur.rle_compression('abbcccaabbbc')
print(amateur_compressed)

amateur_uncompressed = RLEAmateur.rle_uncompression('a1b2c3a2b3c1')
print(amateur_uncompressed)
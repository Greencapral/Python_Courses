'''
🎯 Условие

Напишите класс RomanArabicConverter, который будет содержать два метода:

roman_to_arabic(roman_number: str) -> int: принимает строку с римским числом и возвращает его арабский аналог в виде целого числа.

arabic_to_roman(arabic_number: int) -> str: принимает целое число в диапазоне от 1 до 3999 и возвращает его римское представление в виде строки.

📋 Примечания

Обработка римских чисел основана на правилах вычитания (например, IV — это 5 - 1 = 4).

Римская система не поддерживает числа больше 3999 без дополнительных обозначений.

Пример 1

IX -> 9
CDXVII -> 417
MMMCDXCIV -> 3494
Пример 2

17 -> XVII
2222 -> MMCCXXII
3999 -> MMMCMXCIX

'''
roman_digits = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

class RomanArabicConverter:


    @staticmethod
    def roman_to_arabic(roman_number: str) -> int:
        """Преобразует римское число в арабское"""
        temp_lst = []
        res = 0
        k = 0
        i = 0

        for char in roman_number:
            temp_lst.append(roman_digits[char])

        while i < len(temp_lst)-1:
            if temp_lst[i] < temp_lst[i+1]:
                res = res + temp_lst[i+1] - temp_lst[i] -k
                i += 1
                k = 0
            elif temp_lst[i] > temp_lst[i+1]:
                res = res + temp_lst[i] + k
                k = 0
            else:
                k = k + temp_lst[i]
                if i == len(temp_lst)-2:
                    res = res + k + temp_lst[i+1]
            i += 1

        return res





    @staticmethod
    def arabic_to_roman(arabic_number: int) -> str:
        """Преобразует арабское число в римское."""
        res = ''
        th_d = arabic_number // 1000
        tu_d = (arabic_number - 1000 * th_d) // 100
        doz = (arabic_number - 1000 * th_d - 100 * tu_d) // 10
        ones = (arabic_number - 1000 * th_d - 100 * tu_d - 10 * doz)

        for i in range(th_d):
            res = res + 'M'

        if tu_d == 9:
            res = res + 'CM'
        elif tu_d == 8:
            res = res + 'DCCC'
        elif tu_d == 7:
            res = res + 'DCC'
        elif tu_d == 6:
            res = res + 'DC'
        elif tu_d == 5:
            res = res + 'D'
        elif tu_d == 4:
            res = res + 'CD'
        elif tu_d == 3:
            res = res + 'CCC'
        elif tu_d == 2:
            res = res + 'CC'
        elif tu_d == 1:
            res = res + 'C'

        if doz == 9:
            res = res + 'XC'
        elif doz == 8:
            res = res + 'LXXX'
        elif doz == 7:
            res = res + 'LXX'
        elif doz == 6:
            res = res + 'LX'
        elif doz == 5:
            res = res + 'L'
        elif doz == 4:
            res = res + 'XL'
        elif doz == 3:
            res = res + 'XXX'
        elif doz == 2:
            res = res + 'XX'
        elif doz == 1:
            res = res + 'X'
            
        if ones == 9:
            res = res + 'IX'
        elif ones == 8:
            res = res + 'VIII'
        elif ones == 7:
            res = res + 'VII'
        elif ones == 6:
            res = res + 'VI'
        elif ones == 5:
            res = res + 'V'
        elif ones == 4:
            res = res + 'IV'
        elif ones == 3:
            res = res + 'III'
        elif ones == 2:
            res = res + 'II'
        elif ones == 1:
            res = res + 'I'

        return res


# Примеры использования
t1 ='IX'
t2 = 'CDXVII'
t3 = 'MMMCDXCIV'

converter = RomanArabicConverter()



# Преобразование римского числа в арабское
arabic_number1 = converter.roman_to_arabic('XVII')
arabic_number2 = converter.roman_to_arabic(t1)
arabic_number3 = converter.roman_to_arabic(t2)
arabic_number4 = converter.roman_to_arabic(t3)


print(arabic_number1)  # Вывод: 417
print(arabic_number2)
print(arabic_number3)
print(arabic_number4)

# Преобразование арабского числа в римское
roman_number = converter.arabic_to_roman(17)
roman_number1 = converter.arabic_to_roman(2222)
roman_number2 = converter.arabic_to_roman(3999)
print(roman_number)
print(roman_number1)  # Вывод: MMCCXXII
print(roman_number2)

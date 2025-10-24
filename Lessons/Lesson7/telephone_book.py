'''
Домашнее задание
Создание телефонного справочника

Цель:
Написать телефонный справочник, который будет сохранять контакты в файл и иметь следующий функционал:

открыть файл
сохранить файл
показать все контакты
создать контакт
найти контакт
изменить контакт
удалить контакт
выход

Описание/Пошаговая инструкция выполнения домашнего задания:
Пояснения и рекомендации:

Данное задание можно выполнить в двух вариантах: использовать готовый файл с контактами (находится в материалах) или написать свою структуру:
В качестве "хранилища" контактов можно использовать любой формат - txt, json, csv
Контакт минимально должен содержать имя, телефон и комментарий (по желанию можно дополнить поля)
Реализацию сохранения можно выполнить двумя способами: загружать файл, создавать буферную копию для работы и в дальнейшем сохранять (или нет) внесенные изменения, или вносить изменения сразу в файл
Если выбран вариант буферизации - добавить функционал проверки изменений перед выходом (предлагать сохранить изменения) - опционально (делать необязательно)
Поиск по контактам можно делать отдельно по полям (имя, телефон, комментарий), так и общий (поисковое слово ищет сразу во всех полях контакта)
Для упрощения поиска, изменения и удаления рекомендуется добавить контактам - ID
Добавить всевозможные проверки, чтобы программа не крашилась в случае введенных неверных данных
Данное задание подразумевает отличное владение всеми навыками, затронутыми в первом модуле
Сдавать ДЗ ссылкой на свой репозиторий.

Критерии оценки:
создание меню
открыть файл
сохранить файл
показать все контакты
создать контакт
найти контакт
изменить контакт
удалить контакт
1 балл за каждый верно написанный блок
2 балла за полностью рабочий телефонный справочник
'''
import time

import json

CONTACT = {
    'ID': '',
    'Name': '',
    'Surname': '',
    'Phone': '',
    'Email': '',
    'Coments': ''
}

MAX_ID = 0


def menu():
    print('-' * 25)
    print('Добро пожаловать в лучший телефонный справочник на этом компьютере!')
    print('Пожалуйста, введите номер пункта для выбора операции:')
    print('-' * 25)
    print('[1] - Показать все имеющиеся контакты')
    print('[2] - Создать новый контакт')
    print('[3] - Редактировать имеющиеся контакт')
    print('[4] - Найти контакт')
    print('[5] - Удалить контакт')
    print('[6] - Выход')
    print('-' * 25)


def file_save():
    t = file_load()
    t.append(CONTACT)
    with open('contact.json', 'a', encoding='utf-8') as file:
        json.dump(t, file, indent=4, ensure_ascii=False)



def file_load():
    data = []
    try:
        with open('contact.json', 'r', encoding='utf-8') as file:
            context = file.read().strip()
            if not context:
                return []
            else:
                return json.load(context)
    except FileNotFoundError:
        with open('contact.json', 'a', encoding='utf-8') as file:
            return []


def show_all_contacts():
    pass


def new_contact():
    global CONTACT
    allID = []

    print('\n')
    print('*' * 25)
    print('Создание нового контакта:\n')
    CONTACT['Name'] = input('Введите имя:')
    CONTACT['Surname'] = input('Введите фамилию:')
    CONTACT['Phone'] = input('Введите номер телефона:')
    CONTACT['Email'] = input('Введите адрес электронной почты:')
    CONTACT['Comments'] = input('Введите комментарии:')
    print('*' * 25)
    print('Вы ввели:\n')
    print(f'Имя        : {CONTACT['Name']}')
    print(f'Фамилия    : {CONTACT['Surname']}')
    print(f'Телефон    : {CONTACT['Phone']}')
    print(f'Email      : {CONTACT['Email']}')
    print(f'Комментарии: {CONTACT['Comments']}')

    while True:
        print('*' * 25)
        ansver = input("Всё верно? сохраняем? ('Да'=1, 'нет'=0):")
        if ansver == '1':
            context = file_load()
            for i in context:
                allID.append(i.get('ID'))
            CONTACT['ID'] = 1 if context == [] else max(allID) + 1
            file_save()
            print('*' * 25)
            print('Готово!\nВозвращаемся в главное меню...')
            time.sleep(2)
            break
        elif ansver == '0':
            break
        else:
            print('некорректный ввод, повторите.')
            time.sleep(2)


def search_contact():
    pass


def edit_contact():
    pass


def delete_contact():
    pass


def job_done():
    pass


while True:
    menu()
    choice = input('Ваш выбор: ')
    if choice == '1':
        show_all_contacts()
    elif choice == '2':
        new_contact()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        job_done()
        break
    else:
        print('ваш выбор пока не реализован в справочнике, попробуйте выбрать что-то другое.\n')
        time.sleep(2)
        menu()

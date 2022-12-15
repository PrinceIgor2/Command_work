from user_interface import get_menu_item
from functions import read_from_txt, string_to_list, list_to_string
from functions import find_by_name, write_string_to_txt
def change():
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно изменить\n> ")
    data_1 = read_from_txt('bd.txt', 'UTF-8')
    data_1 = string_to_list(data_1)
    find_data = find_by_name(delete_item, data_1)
    find_data = string_to_list(find_data)

    if len(find)>1:
        print(f"\nПод ваш запрос подходят несколько контактов\n", *find_data)
        print('Уточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()
    elif len(find) == 0:
        print('Не удалось найти контакт\nУточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()
    else:
        print(f"Выбран контакт для изменения\n", *find_data)
        find_data = list_to_string(find_data)
        find_data = str(input("Введите новое значение для контакта через пробел: \n> "))
        find_data = string_to_list(find_data)
        data_1.append(find_data)
        data_1 = string_to_list(data_1)
        data_1 = sorted(data_1)
        data_1 = list_to_string(find_data)
        write_string_to_txt('bd.txt', 'UTF-8', data_1)
        print('Контакт успешно изменён\n')
        resp = input("Продолжить  - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()

change()
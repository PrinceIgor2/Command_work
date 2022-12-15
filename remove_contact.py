import os
import time
from user_interface import get_menu_item
from sty import fg, bg, ef, rs

from functions import read_from_txt, string_to_list, list_to_string
from functions import find_by_name, write_string_to_txt


def delete():
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно удалить\n> ")
    verify_delete  = input(f"Вы действительно хотите удалить контакт со значением >{delete_item}< ? "
                           f"\nНапишите 'да'/'нет'/'q'(выход в меню)\n> ")
    if verify_delete == "да":
        data = read_from_txt('bd.txt', 'UTF-8')
        data = string_to_list(data)
        find_data = find_by_name(delete_item, data)
        find_data = string_to_list(find_data)

        if len(find_data) == 0:
            resp = input("Не найдено контактов по заданным параметрам. Хотите уточнить свой запрос?"
                  "\nНапишите 'да'/'q'(выход в меню)(\n>")
            delete() if resp.lower() == 'да' else get_menu_item()

        elif len(find_data) == 1:
            data = [i for i in data if not i in find_data]
            data = list_to_string(data)
            read_from_txt('bd.txt', 'UTF-8', data)
            print('Контакт успешно удален')
        elif len(find_data) > 1:
            print(f"Под ваш запрос подходят несколько контактов\n", find_data)
            accept = input("Хотите удалить все выбранные контакты? 'да'/'нет'/'q'(выход в меню) \n> ")
            if accept == 'да':
                data = [i for i in data if not i in find_data]
                data = list_to_string(data)
                write_string_to_txt('bd.txt', 'UTF-8', data)
                print('Контакты успешно удалены')
                time.sleep(2)
                get_menu_item()
            elif accept.lower() == 'нет':
                print('Уточните свой запрос\n')
                delete()
            else:
                get_menu_item()
    elif verify_delete == "q":
        get_menu_item()
    else:
        delete()

delete()

def delete_all():
    print('Вы вошли в меню полного удаления всех контактов\n')

    resp_1 = input('Хотите продолжить?\nда/нет\n> ')
    if resp_1.lower() != 'да':
        get_menu_item()
    resp_2 = input('Вы уверены что хотите удалить все контакты?\nда/нет\n> ')
    if resp_2.lower() != 'да':
        get_menu_item()
    path = '/Command_work/bd.txt'
    os.remove(path)

delete()




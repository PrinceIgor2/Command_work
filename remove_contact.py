import os
import time
from user_interface import get_menu_item
from sty import fg, bg, ef, rs

from functions import read_from_txt, string_to_list, list_to_string
from functions import find_by_name, write_string_to_txt

path = 'phone_db.txt'
def delete():
    '''
        Функция позволяет удалить один или несколько выбранных
        пользователем контактов
    '''
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно удалить\n> ")
    verify_delete  = input(f"Вы действительно хотите удалить контакт со значением >{delete_item}< ? "
                           f"\nНапишите 'да'/'нет'/'q'(выход в меню)\n> ")
    if verify_delete == "да":
        data = read_from_txt(path, 'UTF-8')
        data = string_to_list(data)
        find_data = find_by_name(delete_item, data)
        data = [i for i in data if i not in find_data]
        if len(find_data) == 0:
            resp = input("Не найдено контактов по заданным параметрам. Хотите уточнить свой запрос?"
                  "\nНапишите 'да'/'q'(выход в меню)(\n>")
            if resp.lower() == 'да':
                delete()

        elif len(find_data) == 1:
            print(*find_data)
            data = list_to_string(data)
            write_string_to_txt(path, 'UTF-8', data)
            print('Контакт успешно удален')
        elif len(find_data) > 1:
            print(f"Под ваш запрос подходят несколько контактов\n", *find_data)
            accept = input("Хотите удалить все выбранные контакты? 'да'/'нет'/'q'(выход в меню) \n> ")
            if accept == 'да':
                data = list_to_string(data)
                add_string_to_txt(path, 'UTF-8', data)
                print('Контакты успешно удалены')
                time.sleep(2)
            elif accept.lower() == 'нет':
                print('Уточните свой запрос\n')
                delete()
            else:
                pass
    else:
        pass

if __name__ == '__main__':
    delete()

def delete_all():
    '''
        Функция удаляет всю базу данных
    '''
    print('Вы вошли в меню полного удаления всех контактов\n')

    resp_1 = input('Хотите продолжить?\nда/нет\n> ')
    if resp_1.lower() != 'да':
        pass
    resp_2 = input('Вы уверены что хотите удалить все контакты?\nда/нет\n> ')
    if resp_2.lower() != 'да':
        pass
    path_1 = '/Command_work/bd.txt'
    os.remove(path_1)





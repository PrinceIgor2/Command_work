import os
import time

from functions import read_from_txt, string_to_list, list_to_string
from functions import write_string_to_txt, add_string_to_txt
from find_contact import find

def delete():
    '''
        Функция позволяет удалить один или несколько выбранных
        пользователем контактов
    '''
    path = 'phone_db.txt'
    print("Вы вошли в меню удаления контактов")
    find_data = find()
    if len(find_data) == 0:
        delete()
    verify_delete  = input(f"Вы действительно хотите удалить контакт? "
                           f"\nНапишите 'да'/'нет'/'q'(выход в меню)\n> ")
    if verify_delete == "да":
        data = read_from_txt(path, 'UTF-8')
        data = string_to_list(data)
        data = [i for i in data if i not in find_data]
        data = list_to_string(data)
        write_string_to_txt(path, 'UTF-8', data)
        print('Контакт успешно удален')
    else:
        pass


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





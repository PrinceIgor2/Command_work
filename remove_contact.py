import os
import time
from user_interface import get_menu_item
from sty import fg, bg, ef, rs
def delete():
    new,kash_del = [],[]
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно удалить\n> ")
    verify_delete  = input(f"Вы действительно хотите удалить контакт со значением >{delete_item}< ? "
                           f"\nНапишите 'да'/'нет'/'q'(выход в меню)\n> ")
    if verify_delete == "да":
        for  item  in read_data_string(bd.txt, 'UTF-8'):
            for i in item:
                if delete_item.lower()


        with open('bd.txt', 'r', encoding = 'UTF-8') as file:
            for line in file:
                if delete_item.lower() not in line.lower():
                    new.append(line)
                else:
                    kash_del.append(line)
        if len(kash_del) == 0:
            resp = input("Не найдено контактов по заданным параметрам. Хотите уточнить свой запрос?"
                  "\nНапишите 'да'/'q'(выход в меню)(\n>")
            delete() if resp.lower() == 'да' else get_menu_item()

        elif len(kash_del) == 1:
            with open('bd.txt', 'w') as file:
                file.writelines(new)
            print('Контакт успешно удален')
        else:
            print(f"Под ваш запрос подходят несколько контактов\n", *kash_del)
            accept = input("Хотите удалить все выбранные контакты? 'да'/'нет'/'q'(выход в меню) \n> ")
            if accept.lower() == 'да':
                with open('bd.txt', 'w', encoding = 'UTF-8') as file:
                    file.writelines(new)
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

# delete()

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




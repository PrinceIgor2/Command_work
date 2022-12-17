from user_interface import get_menu_item
from functions import read_from_txt, string_to_list, list_to_string
from functions import find_by_name, write_string_to_txt
def change():
    path = 'bd.txt'
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно изменить\n> ")
    data_1 = read_from_txt(path, 'UTF-8')
    data_1 = string_to_list(data_1)
    find_data = find_by_name(delete_item, data_1)
    print(find_data)

    if len(find_data)>1:
        print(f"\nПод ваш запрос подходят несколько контактов\n", *find_data)
        print('Уточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()
    elif len(find_data) == 0:
        print('Не удалось найти контакт\nУточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()
    else:
        data_1 = [i for i in data_1 if i not in find_data]
        print(f"Выбран контакт для изменения\n", *find_data)
        new_data = list(map(str,input("Введите новое значение для контакта через пробел: \n> ").split(" ")))
        # new_data = list(map(str,split(' ')))
        data_1.append(new_data)
        data_1.sort()
        data_1 = list_to_string(data_1)
        write_string_to_txt('bd.txt', 'UTF-8', data_1)
        print('Контакт успешно изменён\n')
        resp = input("Продолжить  - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()

if __name__ == '__main__':
    change()
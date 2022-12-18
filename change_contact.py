from user_interface import get_menu_item
from functions import read_from_txt, string_to_list, list_to_string
from functions import find_by_name, write_string_to_txt

def change():    
    '''
        Функция позволяет изменить выбранный пользователем контакт
    '''
    path = 'phone_db.txt'
    delete_item = input("введите данные контакта, который нужно изменить\n> ")
    data_1 = read_from_txt(path, 'UTF-8')
    data_1 = string_to_list(data_1)
    find_data = find_by_name(delete_item, data_1)
    # find_data = string_to_list(find_data)

    if len(find_data)>1:
        print(f"\nПод ваш запрос подходят несколько контактов\n", *find_data)
        print('Уточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        if resp.lower() == 'да':
            change()
    elif len(find_data) == 0:
        print('Не удалось найти контакт\nУточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        if resp.lower() == 'да':
            change()
    else:
        data_1 = [i for i in data_1 if i not in find_data]
        print(f"Выбран контакт для изменения\n", *find_data)
        find_data = list(map(str,input("Введите новое значение для контакта через пробел: \n> ").split()))
        data_1.append(find_data)
        data_1 = list_to_string(data_1)
        write_string_to_txt(path, 'UTF-8', data_1)
        print('Контакт успешно изменён\n')
        resp = input("Продолжить  - 'да', Выйти в главное меню - 'любой символ':\n>")
        if resp.lower() == 'да':
            change()

if __name__ == '__main__':
    change()
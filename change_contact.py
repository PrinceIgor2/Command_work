from user_interface import get_menu_item
from functions import read_from_txt, string_to_list, list_to_string
from functions import write_string_to_txt, add_string_to_txt
from find_contact import find

def change():
    '''
        Функция позволяет изменить выбранный пользователем контакт
    '''
    print("Вы вошли в меню редактирования контактов")
    path = 'phone_db.txt'

    data_1 = read_from_txt(path, 'UTF-8')
    data_1 = string_to_list(data_1)
    find_data = find()

    if len(find_data) == 0:
        change()
    else:
        data_1 = [i for i in data_1 if i not in find_data]
        print(f"Выбран контакт для изменения\n")
        find_data = list(map(str, input("Введите новое значение для контакта через пробел: \n> ").split()))
        data_1.append(find_data)
        data_1 = list_to_string(data_1)
        write_string_to_txt(path, 'UTF-8', data_1)
        print('Контакт успешно изменён\n')


from user_interface import get_menu_item
def change():
    find,last,res = [],[],[]
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно изменить\n> ")
    with open('bd.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if delete_item.lower() not in line.lower():
                last.append(line)
            else:
                find.append(line)
    if len(find)>1:
        print(f"\nПод ваш запрос подходят несколько контактов\n", *find)
        print('Уточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()
    elif len(find) == 0:
        print('Не удалось найти контакт\nУточните свой запрос\n')
        resp = input("Продолжить - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()
    else:
        print(f"Выбран контакт для изменения\n", *find)
        find[0] = input("Введите новое значение для контакта: \n> ")
        res = last+find
        with open('bd.txt', 'w', coding='utf-8') as file:
            for item in sorted(res):
                if '\n' in item:
                    file.write(f'{item}')
                else:
                    file.write(f'{item}\n')
        print('Контакт успешно изменён\n')
        resp = input("Продолжить  - 'да', Выйти в главное меню - 'любой символ':\n>")
        change() if resp.lower() == 'да' else get_menu_item()

change()
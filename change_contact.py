def change_contact():
    delete_item = input("Введите фамилию / фамилию и имя / номер телефона контакта, который нужно изменить\n> ")
    find = []
    last = []
    with open('bd.txt', 'r') as file:
        for line in file:
            if delete_item.lower() not in line.lower():
                last.append(line)
            else:
                find.append(line)

    if len(find)>1:
        print(f"\nПод ваш запрос подходят несколько контактов\n", *find)
        print('Уточните свой запрос\n')
        change_contact()
    elif len(find) == 0:
        print('Не удалось найти контакт\nУточните свой запрос\n')
        change_contact()
    else:
        print(f"Выбран контакт для изменения\n", *find)
        sear = input("Введите новое значение для контакта: \n> ")
        find[0] = '\n' + sear
        res = []
        res = last+find
        with open('bd.txt', 'w') as file:
            for item in res:
                file.write(f'{item}')
        print('Контакт успешно изменён\nХотите вернуться в главное меню?')
        # Неплохо было бы после отфильтровать полученный список(только нужно опред,
        #по какому принципу будем приводить в порядок(буква фамилии к примеру)
        #Здесь будет проверка и возврат в главное меню
change_contact()


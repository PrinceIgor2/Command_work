def delete_element():
    new = []
    kash_del = []
    delete_item = input("Введите фамилию (фамилию и имя или номер телефона) контакта, который нужно удалить\n> ")
    verify_delete = "да"
    verify_delete  = input(f"Вы действительно хотите удалить контакт со значением >{delete_item}< ? \nНапишите 'да' или 'нет'\n> ")
    if verify_delete == "да":
        with open('bd.txt', 'r') as file:
            for line in file:
                if delete_item.lower() not in line.lower():
                    new.append(line)
                else:
                    kash_del.append(line)
        if len(kash_del) == 0:
            print('Не найдено контактов по заданным параметрам. Уточните свой запрос')
            delete_element()
        elif len(kash_del) == 1:
            with open('bd.txt', 'w') as file:
                file.writelines(new)
            print('Контакт успешно удален')
        else:
            print (f"Под ваш запрос подходят несколько контактов\n", *kash_del)
            accept = input("Хотите удалить все выбранные контакты? да/нет \n> ")
            if accept.lower() == 'да':
                with open('bd.txt', 'w') as file:
                    file.writelines(new)
                print('Контакты успешно удалены')
            else:
                print('Уточните свой запрос\n')
                delete_element()

    else:
        delete_element()
#Сюда можно еще допилить кнопку выхода в главное меню на любом из этапов, когда главное меню появится

# delete_element()

def delete_all_element():
    print("\033[31m{}".format('Вы вошли в меню полного удаления всех контактов'))
    resp_1 = input('Хотите продолжить?\nда/нет\n> ')
    #если да, возврат в менюшку, нет продолжаем
    resp_2 = input('Вы уверены что хотите удалить все контакты?\nда/нет\n> ')
    #если да, возврат в менюшку, нет продолжаем и все удаляем
    with open('bd.txt', 'w') as file:
        file.writelines('')

# delete_all_element()
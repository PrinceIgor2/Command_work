from functions import read_from_txt, string_to_list, list_to_string

def find():
    file_path = 'phone_db.txt'
    read_data = read_from_txt(file_path, 'UTF-8')
    pb = string_to_list(read_data)
    
    # Данная функция реализует поиск существующего контакта и выводит результат
    choice = int(input("\n1. Фамилия\n2. Имя\n3. Номер телефона\n4. Коммментарий)\
  \nВыберите критерий поиска: >"))
    query = ""
    temp = []

    if choice == 1:
        # Реализация поиска по имени контакта
        query = str(input("Введите фамилию контакта для поиска: "))

    elif choice == 2:
        # Реализация поиска по фамилии контакта
        query = str(input("Введите имя контакта для поиска: "))

    elif choice == 3:
        # Реализация поиска по номеру телефона контакта
        query = int(input("Введите номер телефона контакта для поиска: "))

    elif choice == 4:
        # Реализация поиска по комментарию к контакту
        query = str(input("Введите комментарий к контакту для поиска: "))
    else:
        print("Неверный критерий поиска, дружок!")
        return

    for i in range(len(pb)):
        if query == pb[i][choice - 1]:
            temp.append(pb[i])
            
    
    if len(temp) == 0:
        print(f"Попробуй поискать еще разок\n {list_to_string(pb)}")
    else: 
        print('Найдено:\n', list_to_string(temp))

    return temp


# Пояснения для Сергея
# 1. pb - меняем на наименование нашего списка контактов
# 2.что-то запутался с форматированием. Примени, пожалуйста, shift+alt+F)))
# 3.добавил функцию"показать содержимое всей книги" / На всякий случай)))

import sys

def find_contact(pb):
	# Данная функция реализует поиск существующего контакта и выводит результат
	choice = int(input("Выберите критерий поиска\n\n\1. Имя\n2. Фамилия\n3. Номер телефона\n4. Коммментарий)\
	\n Пожалуйста, введите: "))
		
	temp = []
	check = -1
	
	if choice == 1:
	# Реализация поиска по имени контакта
		query = str(input("Введите имя контакта для поиска: "))
		for i in range(len(pb)):
			if query == pb[i][0]:
				check = i
				temp.append(pb[i])

    elif choice == 2: 
        # Реализация поиска по фамилии контакта
        query = str(input("Введите фамилию контакта для поиска: "))
		for i in range(len(pb)):
			if query == pb[i][1]:
				check = i
				temp.append(pb[i])
				
	elif choice == 3:
	# Реализация поиска по номеру телефона контакта
		query = int(input("Введите номер телефона контакта для поиска: "))
		for i in range(len(pb)):
			if query == pb[i][2]:
				check = i
				temp.append(pb[i])
				
	elif choice == 4:
	# Реализация поиска по комментарию к контакту
		query = str(input("Введите комментарий к контакту для поиска: "))
		for i in range(len(pb)):
			if query == pb[i][3]:
				check = i
				temp.append(pb[i])
		
		
	else:
    # Если пользователь вводит любой другой символ, поиск не реализуется
	    print("Неверный критерий поиска, дружок!")
		return -1
	
	if check == -1:
        # Указывает на то, что критерию запроса не  было найдено соответствий
	else:
        return -1
	
	else:
		display_all(temp)
		return check
		


# Функция показывает все содержимое телефонной книги
def display_all(pb):
    if not pb:
	# Если функция будет вызвана после удаления всех контактов, появится следующее сообщение
        print("Список контактов пуст: []")
	else:
		for i in range(len(pb)):
		    print(pb[i])






# Еще 1 вариант функции поиска контакта (попроще)

# def find_contact():
#     where_contact = []
#     choice = int(input('По какому полю ищем (0-имя, 1-фамилия, 2-телефон, 3-комментарий): '))
#     find = input('Введите сравниваемое значение: ')
#     for i in range(0, len(model.phonebook)):
#         contact = model.phonebook[i].split('; ')
#         if contact[choice] == find:
#             where_contact.append(i)
#     if where_contact == []:
#         print('Совпадений не найдено')
#     else:
#         print(f'Найдено совпадение в строке {where_contact}')

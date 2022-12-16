
import sys
from functions import read_from_txt, string_to_list


def find():
  file_path = 'phone_db.txt'
  read_data = read_from_txt(file_path, 'UTF-8')
  pb = string_to_list(read_data)
  # Данная функция реализует поиск существующего контакта и выводит результат
  choice = int(input("Выберите критерий поиска\n\n\1. Имя\n2. Фамилия\n3. Номер телефона\n4. Коммментарий)\
  \n Пожалуйста, введите: "))

  temp = []
 
  if choice == 1:
  # Реализация поиска по имени контакта
    query = str(input("Введите имя контакта для поиска: "))    

  if choice == 2:    
    # Реализация поиска по фамилии контакта
    query = str(input("Введите фамилию контакта для поиска: "))        
        
  if choice == 3:
    # Реализация поиска по номеру телефона контакта
    query = int(input("Введите номер телефона контакта для поиска: "))
            
  if choice == 4:
  # Реализация поиска по комментарию к контакту
    query = str(input("Введите комментарий к контакту для поиска: "))
    
  for i in range(len(pb)):
      if query == pb[i][choice - 1]:
        temp.append(pb[i])        

  else:
    print("Неверный критерий поиска, дружок!")

    print(f"Попробуй поискать еще разок {string_to_list(temp)}")






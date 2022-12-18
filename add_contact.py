from functions import give_str_num, add_string_to_txt
from functions import give_int_num, write_string_to_txt, list_to_string


def input_firstname()->str:
    """_Ввод фамилии, если пользователь ввел фамилию
    с маленькой буквы- исправит на большую_

    Returns:
        _str_: _фамилия_
    """
    first = input( "Введите фамилию: ") 
    
    if len(first) > 15:
        input_firstname()
    else: return first.title()

def input_lastname()->str: 
    last = input( "Введите имя: ")
    if len(last) > 15:
        input_lastname()
    else: return last.title()

 
def add(): 
    """_Добавление контакта в файл и проверка номера телефона на число и минимальное и максимальное количество символов_
    """
	
    filename = 'phone_db.txt'
    firstname = input_firstname() 
    lastname = input_lastname() 
    phone_number = give_str_num( "Номер телефона: ", 3, 13) # проверка телефона 
    comment = input('Введите комментарий: ')
    contact_details = f'{firstname} {lastname} {phone_number} {comment} \n' #формируем итоговую строку
    add_string_to_txt(filename, 'UTF-8', contact_details) #запись в файл 
    print(f'Контакт:\n  {contact_details} сохранен!') 


def create_db():

    check = give_int_num('Введите 1 если ходите создать список контактов (существующий будет очищен!), 0 - выйти > ', min_num=0, max_num=1)
    if check == 1:    
        zagolovok = [['фамилия', 'имя', 'телефон', 'комментарий']]
        path_file = 'phone_db.txt'
        write_string_to_txt(path_file, 'utf-8', list_to_string(zagolovok))

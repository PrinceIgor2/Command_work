from functions import give_str_num, add_string_to_txt

filename = 'phone_db.txt'

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
    firstname = input_firstname() 
    lastname = input_lastname() 
    phone_number = give_str_num( "Номер телефона: ", min_num=3, max_num=13) # проверка телефона 
    #phone_number = str(phone_number)
    comment = input('Введите комментарий: ')
    contact_details = f'{firstname} {lastname} {phone_number} {comment} \n' #формируем итоговую строку
    add_string_to_txt(filename, 'UTF-8', contact_details) #запись в файл 
    # myfile = open(filename, "a", encoding='UTF-8') 
    # myfile.write(contact_details) 
    print(f'Контакт:\n  {contact_details} сохранен!') 

add()
from functions import give_int_num, add_string_to_txt

filename = 'phone_db.txt'

def input_firstname():
    """_Ввод фамилии, если пользователь ввел фамилию
    с маленькой буквы- исправит на большую_

    Returns:
        _str_: _фамилия_
    """
    first = input( "Введите фамилию: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 

def input_lastname(): 
    last = input( "Введите имя: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname

 
def add(): 
    """Создаем контакт
    """
    firstname = input_firstname() 
    lastname = input_lastname() 
    phone_number = give_int_num( "Номер телефона: ", min_num=100, max_num=99999999999) 
    phone_number = str(phone_number)
    comment = input('Введите комментарий: ')
    contact_details = f'{firstname} {lastname} {phone_number} {comment}'
    add_string_to_txt(filename, 'UTF-8', contact_details)
    # myfile = open(filename, "a", encoding='UTF-8') 
    # myfile.write(contact_details) 
    print(f'Контакт:\n  {contact_details} сохранен!') 

add()
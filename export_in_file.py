import csv
from functions import give_int_num, read_from_txt, write_string_to_txt, read_from_csv 
from functions import find_by_name, list_to_string, string_to_list, write_list_to_csv
from find_contact import find

def export():
     
    file = 'phone_db.txt'
    coding = 'utf-8' 

    spicok = string_to_list(read_from_txt(file, coding))
    
    check = give_int_num('Введите 1 если ходите экспортировать все контакты, 2 конкретный контакт > ', min_num=1, max_num=2)
    if check == 2:        
        find_spicok = find()
        # если список пустой....
        find_spicok.insert(0, ['фамилия', 'имя', 'телефон', 'комментарий'])        
        cont = 'контакт экспортирован'
    else:
        find_spicok = spicok[:]
        cont = 'контакты экспортированы'

    text_format = input('в каком формте сохранить данные? 1 - txt, 2 - csv > ')   

    if text_format == 1:
        path_file = 'export_phone.txt'
        write_string_to_txt(path_file, coding, list_to_string(find_spicok))
        
    else:
        path_file = 'export_phone.csv'
        write_list_to_csv(path_file, coding, find_spicok)
        
    print(f'{cont} в файл {path_file}')


if __name__ == '__main__':
    export()

from functions import give_int_num, read_from_txt, write_string_to_txt
from functions import list_to_string, string_to_list, write_list_to_csv
from find_contact import find

def export() -> None:
    '''
    Функция позволяет экспортировать один, несколько выбранных или весь список контактов
    в файл 'export_phone.txt' или 'export_phone.csv' по выбору пользователя
    '''
     
    file = 'phone_db.txt'
    coding = 'utf-8' 
    cont = 'контакты экспортированы'
    spisok = string_to_list(read_from_txt(file, coding))
    
    check = give_int_num('Введите 1 если ходите экспортировать все контакты, 2 конкретный контакт > ', min_num=1, max_num=2)
    if check == 2:        
        find_spicok = find()    
        if len(find_spicok) == 0:
            print(f"\nНичего не найдено, попробуте заново")
            return
        elif len(find_spicok) > 1: 
            print('Найдено несколько контактов:')
            lst = (list_to_string(find_spicok)).split('\n')            
            print(list(enumerate(lst, start = 1)))
            
            choise = give_int_num('Выбрать контакт - 1, экспортировать все - 2: > ', min_num=1, max_num=2 ) 
            if choise == 1:                
                num = give_int_num('введите номер экспортируемого контакта: > ', min_num=1, max_num = len(find_spicok))
                find_spicok = find_spicok[num-1:num] 
                cont = 'контакт экспортирован'
        find_spicok.insert(0, ['фамилия', 'имя', 'телефон', 'комментарий'])                
    else:
        find_spicok = spisok[:]
        

    choise_format = give_int_num('в каком формате сохранить данные? 1 - txt, 2 - csv > ', min_num=1, max_num=2)   

    if choise_format == 1:
        path_file = 'export_phone.txt'
        write_string_to_txt(path_file, coding, list_to_string(find_spicok))
        
    else:
        path_file = 'export_phone.csv'
        write_list_to_csv(path_file, coding, find_spicok)
                 
        
    print(f'{cont} в файл {path_file}')


if __name__ == '__main__':
    export()

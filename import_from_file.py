from typing import List, Optional
from os import path
import os.path
import csv

def write_to_csv(path_file: str, coding: str, list_to_write: List[List[str]]):
    """
    Записывает список в файл 

    Args:
    path_file - путь до файла, 
    coding - кодировка ('utf-8'),
    list_to_write - список для записи
    """
    with open(path_file, 'a+', encoding=coding) as w_file:
            file_writer = csv.writer(w_file, delimiter = "," , lineterminator="\n")
            for row in list_to_write:       
                file_writer.writerow(row)

def write_string_to_txt(path_file_phone_db: str, data_txt: str, coding: str):
    """
    Записывает строку в файл 

    Args:
    path_file - путь до файла, 
    coding - кодировка ('utf-8'),
    """  
    with open(path_file_phone_db, 'a+', encoding=coding) as w_file:
        w_file.write(f'\n')
        for i in data_txt:
            w_file.write(f'{i}')

def read_from_csv_wo_header(path_file: str, coding: str, delim:str ):
    """
    Считывает csv файл (без заголовка) и возвращает строку 

    Args:
    path_file - путь до файла,
    coding - кодировка ('utf-8')
    delim - разделитель (по умолчанию ',')

    Returns:
    List[List[str]] - список
    """ 
    list_file = []
    with open(path_file, 'r', encoding=coding) as r_file:    
        file_reader = csv.reader(r_file, delimiter = delim)  
        next(file_reader)
        for row in file_reader:
            list_file.append(row) 
    return list_file

def read_from_txt_wo_header(path_file: str, coding: str) -> str:
    """
    Считывает txt файл и возвращает строку (без заголовка)

    Args:
    path_file - путь до файла,
    coding - кодировка ('utf-8')

    Returns:
    str - строка
    """    
    with open(path_file, 'r', encoding=coding) as r_file:    
        data = r_file.readlines()[1:]
    return(data)

def import_data(path_file_phone_db, coding):
    """
    Импортирует контакты из файлов с расширением .txt и .csv. 
    Проверяет наличие запрашиваемого файла.

    Args:
    path_file_phone_db - файл куда осуществляется импорт
    coding - кодировка ('utf-8')
    
    Return:
    Делает импорт в указанный файл
    """
    path_file_import = input('Укажите имя файла откуда хотите импортировать контакты -> ')
    if os.path.exists(path_file_import) == True:                                            # проверка на наличие файла
        extension_import = path.splitext(path_file_import)[1]                               # возвращаем кортеж
        extension_phone_db = path.splitext(path_file_phone_db)[1]                               
        if extension_import == extension_phone_db == '.txt':                                                          
            data_txt = read_from_txt_wo_header(path_file_import, coding)
            write_string_to_txt(path_file_phone_db, data_txt, coding)
            print(f'Контакты импортированы из файла {path_file_import} в файл --> {path_file_phone_db}')
        elif extension_import == extension_phone_db == '.csv':
            data_csv = read_from_csv_wo_header(path_file_import, coding, ',')
            write_to_csv(path_file_phone_db, coding, data_csv)
            print(f'Контакты импортированы из файла {path_file_import} в файл --> {path_file_phone_db}')
        else:
            print(f'Невозможно импортировать контакты из файла {path_file_import} в {path_file_phone_db}')
    else:
        print('Нет такого файла')    

if __name__ == '__main__':
    import_data('phone_db.txt', 'utf-8')
    import_data('phone_list.csv', 'utf-8')
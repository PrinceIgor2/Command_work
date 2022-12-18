from functions import read_from_txt_wo_header, write_to_csv, read_from_csv_wo_header
from os import path
import os.path
import csv

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
        extension = path.splitext(path_file_import)[1]                                      # возвращаем кортеж, где 2-ой элемент это расширение файла
        if extension == '.txt':
            data_txt = read_from_txt_wo_header(path_file_import, coding)
            with open(path_file_phone_db, 'a+', encoding=coding) as ph_db:
                ph_db.write(f'\n')
                for i in data_txt:
                    ph_db.write(f'{i}')
        elif extension == '.csv':
            data_csv = read_from_csv_wo_header(path_file_import, coding, ',')
            write_to_csv(path_file_phone_db, coding, data_csv)            
    else:
        print('Нет такого файла')      

if __name__ == '__main__':
    # import_data('phone_db.txt', 'utf-8')
    import_data('phone_list.csv', 'utf-8')
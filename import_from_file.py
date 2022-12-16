from functions import read_from_txt


def import_data(path_file_phone_db, coding):
    path_file_import = input(
        'Укажите путь файла откуда хотите импортировать контакты -> ')
    while True:
        try:
            data = read_from_txt(path_file_import, coding)
            with open(path_file_phone_db, 'a+', encoding=coding) as ph_db:
                ph_db.write(f'\n')
                for i in data:
                    ph_db.write(f'{i}')
            break
        except:
            print(
                'Такого файла не существует. Проверьте и укажите корректный файл для импорта.')
            break
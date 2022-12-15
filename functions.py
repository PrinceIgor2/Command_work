from typing import List, Optional


def give_int_num(input_string: str,
                 min_num: Optional[int] = None,
                 max_num: Optional[int] = None) -> int:
    """
    Выпытывает у пользователя число в диапзоне от  min_num до  mах_num:

    Args:
    input_string - предложение ввода

    Returns:
    int - число
    """
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше, чем {max_num}')
                continue
            return num
        except ValueError:
            print('Похоже это не число, попробуте еще раз')


def read_from_txt(path_file: str, coding: str) -> str:
    """
    Считывает txt файл и возвращает строку 

    Args:
    path_file - путь до файла,
    coding - кодировка ('utf-8')

    Returns:
    str - строка
    """
    with open(path_file, 'r', encoding=coding) as r_file:
        data = r_file.read()
    return (data)


def write_string_to_txt(path_file: str, coding: str, string_line: str):
    """
    Записывает строку в файл 

    Args:
    path_file - путь до файла, 
    coding - кодировка ('utf-8'),
    string_line - строка для записи
    """
    with open(path_file, 'w', encoding=coding) as w_file:
        w_file.write(string_line)


def add_string_to_txt(path_file: str, coding: str, string_line: str):
    """
    Добавляет строку в файл 

    Args:
    path_file - путь до файла,
    coding - кодировка ('utf-8'),
    string_line - строка для записи
    """
    with open(path_file, 'a', encoding=coding) as w_file:
        w_file.write(string_line)


def find_by_name(name: str, list_file: List[List[str]]) -> List[List[str]]:
    """
    возвращает список строк в которых найдено заданное имя {name}

    Args:
    name - имя для поиска,
    list_file - список сформированный read_from_txt вида [[1,2,3],[1,2,3],[1,2,3]]

    Returns:
    List(List(str)) - список списков вид [[1,2,3],[1,2,3],[1,2,3]] 
    """
    find_list = []
    for row in list_file:
        if row[1].lower() == name.lower():
            find_list.append(row)

    return find_list


def string_to_list(string_line: str) -> List[List[str]]:
    """
    Возвращает список строк разденных по '\\n' в виде списка элементов разделенных по пробелу [[1,2,3],[1,2,3],[1,2,3]] 

    Args:
    string:str - строка для преобразования

    Returns:
    List[List[str]] - список списков вид [[1,2,3],[1,2,3],[1,2,3]] 
    """
    list_file = []
    string = string_line.split('\n')
    for i in string:
        list_file.append(i.split(' '))
    return (list_file)


def list_to_string(list_file: List[List[str]]) -> str:
    """
    Возвращает строку вида  item_1\\nitem_2\\n....\\item_n\\n

    Args:
    List[List[str]] - список списков вид [[1,2,3],[1,2,3],[1,2,3]]

    Returns:
    str - строка (item_1\\nitem_2\\n....\\item_n\\n)
    """
    srting = ''
    for row in list_file:
        srting += row[0]+' '+row[1]+' '+row[2]+' '+row[3]+'\n'
    return srting

def give_str_num(input_string: str,
            min_str: Optional[int] = None,
            max_str: Optional[int] = None) -> str:
    """
    Выпытывает у пользователя строку состоящую из чисел длинной от min_str до  mах_str:

    Args:
    input_string - предложение ввода

    Returns:
    str: - строка
    """
    while True:
        try:
            num = input(input_string)
            if not num.isdigit():
                print(f'Вводите только цифры')
                continue
            if len(num) < min_str:
                print(f'Введите строку длиннее {min_str} символов')
                continue
            if len(num)> max_str:
                print(f'Введите строку короче {max_str} символов')
                continue
            return num
        except ValueError:
            print('Что пошло не так, попробуйте еще раз')

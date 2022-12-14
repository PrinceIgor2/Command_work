from typing import Optional

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


def read_data_string(filename: str , coding:  str) -> str:

    with open(filename, 'r', encoding=coding) as file:
        data = file.read()
    return data



def write_string_to_file(filename: str , coding:  str, string: str):

    with open(filename, 'w', encoding=coding) as file:
        file.write(string)




def add_string_to_file(filename: str , coding:  str, string: str):

    with open(filename, 'a', encoding=coding) as file:
        file.write(string)            
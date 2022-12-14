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
    
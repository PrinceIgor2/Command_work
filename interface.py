from constants import ABILITIES as ab
from checks import give_int_num

choose_action = 'выберите пункт меню: '

def get_menu_item() -> int:
    """
    Выводит меню
    Принимает число от пользователя, соответствующее операции, которую он хочет выполнить.
    
    Returns:
    int - число. 
    """

    for i in enumerate(ab, start = 1):
        print(*i)
    num = give_int_num(choose_action, min_num = 1, max_num = len(ab))
    return num


if __name__ == '__main__':
    get_menu_item()
from user_interface import get_menu_item
import add_contact, change_contact
import remove_contact, find_contact
import export_in_file, import_from_file
import sys
import os

def start():
    while True:
        menu_item = get_menu_item()

        if menu_item == 1:
            add_contact.add()

        elif menu_item == 2:
            change_contact.change()

        elif menu_item == 3:
            remove_contact.delete()               

        elif menu_item == 4:
            find_contact.find()
            
        elif menu_item == 5:
            export_in_file.export() 
        
        elif menu_item == 6:
            import_from_file.import_data('phone_db.txt', 'utf-8')
            
        elif menu_item == 7:
            remove_contact.delete_all()


        elif menu_item == 0:
            sys.exit('работа завершена') 
        input('---< для продолжения нажмите Enter >---')   
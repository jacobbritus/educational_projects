from class_ToDoList import ToDoList
from class_Menu import Menu
from class_UserFlow import UserFlow

code_list = ToDoList()

menu_test = Menu()

user = UserFlow(menu_test, code_list)

def main():
    while True:
        code_list.adapt_box_length()
        user.main_page()


main()


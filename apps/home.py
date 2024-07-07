from apps.apps import Apps
import os


class Home:
    def __init__(self) -> Apps:
        self.show_ui()
        self.input_menu_choose()

    def show_ui(self):
        os.system('cls')
        print(f"""
            Welcome to Apa Aja Express
            ==========================
            1.  Order Ticket
            2.  View Routes
            3.  View Train
            4.  Exit
            ==========================
            Choose(1-4) :   
            """)

    def input_menu_choose(self) -> Apps | None:
        try:
            menu = int(input())
            match menu:
                case 1: menu = Apps.ORDER_TICKET
                case 2: menu = Apps.VIEW_ROUTES
                case 3: menu = Apps.VIEW_TRAIN
                case 4: menu = Apps.EXIST
            return menu
        except:
            print("Menu not found")

from apps.apps import Apps


class Home:

    def show_ui(self):
        print("Welcome to Apa Aja Express")
        print("==========================")
        print("1.  Order Ticket")
        print("2.  View Routes")
        print("3.  View Train")
        print("4.  Exit")
        print("==========================")
        return self.input_menu_choose()




    def input_menu_choose(self) -> Apps:
        try:
            menu = int(input("Chosee (1-4) : "))
            match menu:
                case 1: menu = Apps.ORDER_TICKET
                case 2: menu = Apps.VIEW_ROUTES
                case 3: menu = Apps.VIEW_TRAIN
                case 4: menu = Apps.EXIST
            return menu
        except:
            print("Menu not found")

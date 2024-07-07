from apps import apps, home, order_ticket, view_routes, view_train
import os

def main() -> None:
    current_domain: apps.Apps = apps.Apps.HOME
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            match current_domain:
                case apps.Apps.ORDER_TICKET: current_domain = order_ticket.OrderTicket()
                case apps.Apps.VIEW_ROUTES: current_domain = view_routes.ViewRoutes().show_ui()
                case apps.Apps.VIEW_TRAIN: current_domain = view_train.ViewTrain().show_ui()
                case apps.Apps.EXIST: break
                case _: current_domain = home.Home().show_ui()
        except Exception as e:
            input('-')
            print(e)


if __name__ == "__main__":
    main()









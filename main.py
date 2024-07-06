from apps import apps, home, order_ticket, view_routes, view_train


def main() -> None:
    current_domain: apps.Apps = apps.Apps.HOME
    while True:
        try:
            match current_domain:
                case apps.Apps.ORDER_TICKET: order_ticket.OrderTicket()
                case apps.Apps.VIEW_ROUTES: view_routes.ViewRoutes()
                case apps.Apps.VIEW_TRAIN: view_train.ViewTrain()
                case apps.Apps.EXIST: break
                case _: current_domain = home.Home()
        except:
            pass


if __name__ == "__main__":
    main()

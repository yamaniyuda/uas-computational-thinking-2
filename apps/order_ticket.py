from data.train import TRAINT_CLASESS, TRAIN_ROUTES_GRAPH
from utils.dijkstra import Dijkstra
from dashtable import data2rst
from datetime import datetime, timedelta
from apps.apps import Apps
import random

class OrderTicket:
    def __init__(self) -> None:
        self.clasess = TRAINT_CLASESS



    def show_ui(self):
        while True:
            print('Make sure you already check your route before you order ticket')

            self.from_station, self.to_station, self.duration = self.__get_routes()
            self.traint_class, self.cost = self.__get_clasess()
            self.name, self.departure_date, self.departure_time = self.__get_personal_data()
            self.total_cost = self.cost * self.duration

            striptime = datetime.strptime(f'{self.departure_date} {self.departure_time}', '%d/%m/%Y %H:%M')
            new_datetime = striptime + timedelta(hours=self.duration)
            new_datetime_str = new_datetime.strftime('%d/%m/%Y %H:%M')

            self.date_arrives, self.time_arrives = new_datetime_str.split()
            self.traint_number = random.randint(100, 999)
            self.platform = f"{random.randint(1, 10) : 02d}"
            self.seat = f"{random.randint(1, 50) : 02d}"
            
            self.__print_ticket()
            print()

            if input('Order another ticket? (Yes/No) : ').strip().lower() == 'no':
                return None
            return Apps.ORDER_TICKET




    def __get_routes(self):
        while True:
            print('\nWhere do you want to go?')
            from_station = input("From\t\t: ").strip().title()
            to_station = input("To\t\t: ").strip().title()

            if (from_station not in TRAIN_ROUTES_GRAPH) or (to_station not in TRAIN_ROUTES_GRAPH):
                    print("Invalid station entered.")
                    continue

            else:
                dijkstraAlg = Dijkstra(TRAIN_ROUTES_GRAPH)
                sort_path, duration = dijkstraAlg.find_sort_path(from_station, to_station)

                print(f"\nHere is route from {from_station} to {to_station}:")
                print(f"Path\t\t: {' -> '.join(sort_path)}")
                print(f"Duration\t: {duration} hours")
            
            break

        return from_station, to_station, duration
    



    def __get_clasess(self):
        while True:
            print('\nMake sure you already check your belongings before choosing the class')
            choose_classes = input('Choose class (Economy, Business, Exclusive): ').strip().lower()
            class_data = self.clasess.get(choose_classes)

            if class_data is None:
                print(f'There is no {choose_classes.title()} class')
                input()
                continue
            break

        return choose_classes.title(), class_data.get('cost')

        



    def __get_personal_data(self):
        while True:
            print('\nPlease insert your data:')
            name = input('Name '.ljust(50) + ': ')
            departure_date = input('Departure date (DD/MM/YYYY) '.ljust(50) + ': ')
            departure_time = input('Departure time (HH:MM) '.ljust(50) + ': ')
            already_data = input('Are you sure about all the data above ? (Yes/No)'.ljust(50) + ': ').strip().lower()
            
            if already_data == 'no': continue
            return name, departure_date, departure_time
        


    
    def __print_ticket(self):
        print()
        print("+" + "-"  * 60 + "+")
        print(f"|{'TRAINT TICKET':^60}|")
        print("+" + "-"  * 60 + "+")
        print(f"{'|  ORIGIN':<17}: {self.from_station:<42}|")
        print("+" + "-"  * 60 + "+")
        print(f"{'| DATE':<17}: {self.departure_date:<23}{'TIME':<7}: {self.departure_time:<10}|")
        print(f"{'| TRAINT#':<17}: {self.traint_number:<23}{'CLASS':<7}: {self.traint_class:<10}|")
        print(f"{'| PLATFORM':<17}: {self.platform:<23}{'SEAT':<7}: {self.seat:<10}|")
        print("+" + "-"  * 60 + "+")
        print(f"{'| DESTINATION':<17}: {self.to_station:<42}|")
        print(f"{'| DATE':<17}: {self.date_arrives:<23}{'TIME':<7}: {self.time_arrives:<10}|")
        print("+" + "-"  * 60 + "+")
        print(f"{'| PASSENGER NAME':<17} : {self.name:<41}|")
        print("+" + "-"  * 60 + "+")
        print(f"Total cost: ${self.total_cost}")
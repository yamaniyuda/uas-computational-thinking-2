from data.train import TRAINT_CLASESS, TRAIN_ROUTES_GRAPH
from utils.dijkstra import Dijkstra
import random

class TrainTicketSystem:
    def __init__(self) -> None:
        self.clasess = TRAINT_CLASESS



    def show_ui(self):
        print('Make sure you already check your route before you order ticket')
        print('Where do you want to go?')


    def __get_routes(self):
        from_station = input("From\t\t: ").strip().title()
        to_station = input("To\t\t: ").strip().title()

        if (from_station not in TRAIN_ROUTES_GRAPH) or (to_station not in TRAIN_ROUTES_GRAPH):
                print("Invalid station entered.")

        else:
            dijkstraAlg = Dijkstra(TRAIN_ROUTES_GRAPH)
            sort_path, duration = dijkstraAlg.find_sort_path(from_station, to_station)

            print(f"\nHere is the shortest route from {from_station} to {to_station}:")
            print(f"Path\t\t: {' -> '.join(sort_path)}")
            print(f"Duration\t: {duration} hours")
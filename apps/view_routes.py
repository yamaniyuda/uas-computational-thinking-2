from tabulate import tabulate
from apps.apps import Apps
from data.train import TRAINT_COST_HOUR, TRAIN_ROUTES, TRAIN_ROUTES_GRAPH
from utils import dijkstra


class ViewRoutes:

    def show_ui(self):
        headers = ["Routes (2-ways)", "Duration (hours)"]
        table = [[f"{start} -- {end}", duration]
                 for start, end, duration in TRAIN_ROUTES]
        print(f"Cost = ${TRAINT_COST_HOUR}/hour")
        print(tabulate(table, headers, tablefmt="heavy_outline"))
        
        return self.find_route()
    
    

    def find_route(self):
        while True:
            print("\nTake your route")
            from_station = input("From\t\t: ").strip().title()
            to_station = input("To\t\t: ").strip().title()

            if (from_station not in TRAIN_ROUTES_GRAPH) or (to_station not in TRAIN_ROUTES_GRAPH):
                print("Invalid station entered.")
            else:
                dijkstraAlg = dijkstra.Dijkstra(TRAIN_ROUTES_GRAPH)
                sort_path, duration = dijkstraAlg.find_sort_path(from_station, to_station)

                print(f"\nHere is the shortest route from {from_station} to {to_station}:")
                print(f"Path\t\t: {' -> '.join(sort_path)}")
                print(f"Duration\t: {duration} hours")
            
            another_route = input("\nSee another route?\nYes/No = ").strip().lower()
            
            if another_route == 'yes': return Apps.VIEW_ROUTES
            return None
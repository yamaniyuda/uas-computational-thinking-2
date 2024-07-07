from tabulate import tabulate

routes = [
    ('Minstone', 'Cowstone', 3),
    ('Oldcastle', 'New North', 5),
    ('Oldcastle', 'Freeham', 2),
    ('Cowstone', 'Freeham', 5),
    ('Cowstone', 'New North', 4),
    ('Cowstone', 'Bingborough', 6),
    ('Cowstone', 'Donningpool', 7),
    ('Cowstone', 'Highbrook', 2),
    ('New North', 'Bingborough', 4),
    ('New North', 'Donningpool', 6),
    ('New North', 'Wington', 4),
    ('New North', 'Highbrook', 2),
    ('Freeham', 'Cowstone', 2),
    ('Freeham', 'Donningpool', 3),
    ('Freeham', 'Wington', 5),
    ('Bingborough', 'Donningpool', 1),
    ('Bingborough', 'Highbrook', 5),
    ('Donningpool', 'Wington', 4),
    ('Donningpool', 'Highbrook', 5),
    ('Donningpool', 'Old Mere', 2),
]

graph = {}
for start, end, duration in routes:
    if start not in graph:
        graph[start] = {}
    if end not in graph:
        graph[end] = {}
    graph[start][end] = duration
    graph[end][start] = duration

cost_per_hour = 15

class ViewRoutes:
    def __init__(self) -> None:
        pass

    def display_routes(self):
        headers = ["Routes (2-ways)", "Duration (hours)"]
        table = [[f"{start} -- {end}", duration] for start, end, duration in routes]
        print(f"Cost = ${cost_per_hour}/hour")
        print(tabulate(table, headers, tablefmt="grid"))

    def find_route(self):
        while True:
            print("\nTake your route")
            from_station = input("From: ").strip()
            to_station = input("To: ").strip()

            if from_station not in graph or to_station not in graph:
                print("Invalid station entered.")
            else:
                duration, path = dijkstra(graph, from_station, to_station)
                if duration == float("inf"):
                    print(f"No route from {from_station} to {to_station}.")
                else:
                    total_cost = duration * cost_per_hour
                    print(f"\nHere is the shortest route from {from_station} to {to_station}:")
                    print(f"{' -> '.join(path)}")
                    print(f"Duration: {duration} hours")
                    print(f"Cost: ${total_cost}")

            another_route = input("\nSee another route?\nYes/No = ").strip().lower()
            if another_route != 'yes':
                break

if __name__ == "__main__":
    vr = ViewRoutes()
    vr.display_routes()
    vr.find_route()

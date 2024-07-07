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
    def __init__(self, graph) -> None:
        self.graph = graph

    def display_routes(self):
        headers = ["Routes (2-ways)", "Duration (hours)"]
        table = [[f"{start} -- {end}", duration] for start in self.graph for end, duration in self.graph[start].items()]
        print(f"Cost = ${cost_per_hour}/hour")
        print(tabulate(table, headers, tablefmt="grid"))

    def dijkstra(self, start, end):
        from heapq import heappop, heappush
        import math

        pq = [(0, start)]
        dist = {node: math.inf for node in self.graph}
        dist[start] = 0
        prev = {node: None for node in self.graph}

        while pq:
            current_dist, current_node = heappop(pq)

            if current_dist > dist[current_node]:
                continue

            if current_node == end:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = prev[current_node]
                path.reverse()
                return dist[end], path

            for neighbor, weight in self.graph[current_node].items():
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = current_node
                    heappush(pq, (distance, neighbor))

        return math.inf, []

    def find_route(self):
        while True:
            print("\nTake your route")
            from_station = input("From: ").strip().capitalize()
            to_station = input("To: ").strip().capitalize()

            if from_station not in self.graph or to_station not in self.graph:
                duration, path = self.dijkstra(from_station, to_station)
                if duration == float("inf"):
                    print(f"No route from {from_station} to {to_station}.")
                else:
                    total_cost = duration * cost_per_hour
                    print(f"\nHere is the shortest route from {from_station} to {to_station}:")
                    print(f"{' -> '.join(path)}")
                    print(f"Duration: {duration} hours")
                    print(f"Cost: ${total_cost}")
            else:
                print("Invalid station entered.")

            another_route = input("\nSee another route?\nYes/No = ").strip().lower()
            if another_route != 'yes':
                break

if __name__ == "__main__":
    vr = ViewRoutes(graph)
    vr.display_routes()
    vr.find_route()

import heapq


class Dijkstra:
    def __init__(self, graph: dict):
        self.graph = graph
    
    def find_sort_path(self, start: str, destination: str) -> tuple:
        queue = [(0, start)]
        shortest_paths = {start: (None, 0)}
        visited = set()

        while queue:
            (cost, node) = heapq.heappop(queue)

            if node in visited:
                continue

            visited.add(node)

            if node is destination:
                break

            for neighbor, weight in self.graph[node].items():
                if neighbor in visited:
                    continue

                new_cost = cost + weight
                if neighbor not in shortest_paths or new_cost < shortest_paths[neighbor][1]:
                    shortest_paths[neighbor] = (node, new_cost)
                    heapq.heappush(queue, (new_cost, neighbor))

        path = []
        node = destination
        while node is not None:
            path.append(node)
            next_node = shortest_paths[node][0]
            node = next_node

        return path[::-1], shortest_paths[destination][1]
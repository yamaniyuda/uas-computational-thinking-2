import heapq


class Dijkstra:
    def __init__(self, graph: dict, start: str, end: str):
        queue = [(0, start)]
        shortest_paths = {start: (None, 0)}
        visited = set()

        while queue:
            (cost, node) = heapq.heappop(queue)

            if node in visited:
                continue

            visited.add(node)

            if node is end:
                break

            for neighbor, weight in graph[node].item():
                if neighbor in visited:
                    continue

                new_cost = cost + weight
                if neighbor not in shortest_paths or new_cost < shortest_paths[neighbor][1]:
                    shortest_paths[neighbor] = (node, new_cost)
                    heapq.heappush(queue, (new_cost, neighbor))

        path = []
        node = end
        while node is not None:
            path.append(node)
            next_node = shortest_paths[node][0]
            node = next_node

        path[::-1]

        self.path = path
        self.shortest_paths = shortest_paths

        return self

    def print_sort_path(self):
        print(" -> ".join(self.shortest_paths))

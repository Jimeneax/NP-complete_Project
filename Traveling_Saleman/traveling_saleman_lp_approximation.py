from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def longest_path_greedy(self, start):
        visited = set()
        distance = [-float('inf')] * self.vertices
        distance[start] = 0

        for _ in range(self.vertices):
            max_vertex = -1
            max_distance = -float('inf')

            for v in range(self.vertices):
                if v not in visited and distance[v] > max_distance:
                    max_vertex = v
                    max_distance = distance[v]

            visited.add(max_vertex)

            for neighbor, weight in self.graph[max_vertex]:
                if distance[max_vertex] + weight > distance[neighbor]:
                    distance[neighbor] = distance[max_vertex] + weight

        return distance

def main():
    g = Graph(6)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 6)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 5, 1)
    g.add_edge(3, 4, -1)
    g.add_edge(4, 5, -2)

    start_vertex = 1  # You can choose any starting vertex
    result = g.longest_path_greedy(start_vertex)

    print("Longest paths from vertex", start_vertex, ":")
    for i, dist in enumerate(result):
        print(f"To vertex {i}: {dist}")

if __name__ == "__main__":
    main()

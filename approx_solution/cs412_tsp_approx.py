"""
    name:  Alberto Jimenez

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           TSP referenced GeeksforGeeks, Stack Overflow, digitalocean
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import timeit


# The TSP greedy algorithm is being greedy with the shortest path
# to any connected vertices with no regard to the total length of
# the whole traversal. The hope is that by consistently choosing
# the nearest vertices that the algorithm will end up with a
# solution that is reasonably close to the optimal route. 
def nearest_vertex_tsp(graph, n):
    # Initialize visited array to false
    visited = [False] * n
    
    # Initialize path and totatl length to 0
    path = [0]
    total_length = 0

    # Set starting point to true
    visited[0] = True

    # Loop through the remaining vertices
    for _ in range(n - 1):
        current_v = path[-1]
        nearest_v = None
        min_distance = float('inf')

        # Find the nearest unvisited vertex
        for v in range(n):
            if not visited[v] and graph[current_v][v] < min_distance:
                nearest_v = v
                min_distance = graph[current_v][v]

        # Add the nearest vertex to the graph
        path.append(nearest_v)
        visited[nearest_v] = True
        total_length += min_distance

    # Return to the starting vertex to complete the cycle
    path.append(0)
    total_length += graph[path[-2]][0]

    return total_length, path

# Convert char into an int
def index_to_letter(index):
    return chr(index + ord('a'))

def main():
    n, m = map(int, input().split())
    graph_input = [input().split() for _ in range(m)]

    vertices = set()
    for u, v, _ in graph_input:
        vertices.add(u)
        vertices.add(v)
        
    # Create a dictionary to map vertices to indices
    vertex_to_index = {vertex: index for index, vertex in enumerate(vertices)}

    graph = [[0] * n for _ in range(n)]
    
    for u, v, w in graph_input:
        u_index, v_index = vertex_to_index[u], vertex_to_index[v]
        w = float(w)
        graph[u_index][v_index] = w
        graph[v_index][u_index] = w

    length, path = nearest_vertex_tsp(graph, n)
    
    # Print the results
    print (str(length))    
    path_labels = [list(vertex_to_index.keys())[index] for index in path]
    print(" ".join(map(str, path_labels)))

if __name__ == "__main__":
    main()
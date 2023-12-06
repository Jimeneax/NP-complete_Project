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
from itertools import permutations

# TSP Given a set of vertices and weights between every pair of 
# vertices, the problem is to find the shortest possible route that 
# visits every city exactly once and returns to the starting point. 
def tsp(graph, n):
    # Generate all possible permutations of cities
    all_permutations = permutations(range(1, n))

    # Initialize minimum length and path
    min_length = float('inf')
    min_path = None

    for path in all_permutations:
        # Add the starting and ending city to the path
        path = (0,) + path + (0,)
        # Calculate the total length of the path
        length = 0
        for i in range(n):
            length += graph[path[i]][path[i + 1]]

        # Update minimum length and path if needed
        if length < min_length:
            min_length = length
            min_path = path

    return min_length, min_path


# Convert char into an int
def index_to_letter(index):
    return chr(index + ord('a'))


def main():
    n, m = map(int, input().split())
    graph_input = [input().split() for _ in range(m)]
    
    # The start time of the algorithm
    start_time = timeit.default_timer()
    
    # Initialize the graph as an adjacency matrix with zeros
    graph = [[0] * n for _ in range(n)]

    for u, v, w in graph_input:
        # Convert vertices to integers and update the graph
        u, v, w = ord(u) - ord('a'), ord(v) - ord('a'), int(w)
        graph[u][v] = w
        graph[v][u] = w

    length, path = tsp(graph, n)
    
    # Convert the vertices back to letters
    path_letters = [index_to_letter(vertex) for vertex in path]

    # The end time of the algorithm
    end_time = timeit.default_timer()
    
    # Print the results
    print(length)
    print(" ".join(path_letters))
    
    # Display the elapsed time in milliseconds
    print(f"Wall Clock Time: {(end_time - start_time) * 1000} milliseconds")
    
    pass

if __name__ == "__main__":
    main()
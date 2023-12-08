"""
    name:  Alberto Jimenez
    Honor Code and Acknowledgments:
            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
           TSP referenced GeeksforGeeks, Stack Overflow, digitalocean, youtube
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts

import sys
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

    length, path = tsp(graph, n)
    
    # Print the results
    print (str(length))    
    path_labels = [list(vertex_to_index.keys())[index] for index in path]
    print(" ".join(map(str, path_labels)))
     

if __name__ == "__main__":
    main()

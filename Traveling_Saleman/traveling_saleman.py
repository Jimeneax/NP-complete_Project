"""
    name:  Alberto Jimenez Aaron Nyaanga

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           TSP and LP solutions we referenced GeeksforGeeks
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
from sys import maxsize
from itertools import permutations
import heapq


# LP graphs are directed.
def longest_path(graph):
    
    return 0


# TSP Given a set of vertices and weights between every pair of 
# vertices, the problem is to find the shortest possible route that 
# visits every city exactly once and returns to the starting point. 
def tsp(graph, n):
    # stroe all vertex apart 
    vertex = []
    for i in range(n):
        vertex.append(i)
    
    # Stroe minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # Store current path weight
        cur_path_w = 0
        # Compute current path weight
        
        
    
    return min_path


def main():
    # n is the number of vertices, m is the number of edges
    n, m = map(int, input().split())
    # Matrix representaton of the graph
    graph = [tuple(input().split()) for _ in range(m)]


    tsp(graph, n)
    longest_path(graph)
    
    print(graph)
    
    pass

if __name__ == "__main__":
    main()
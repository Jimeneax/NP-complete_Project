"""
    name:  Alberto Jimenez Aaron N

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import sys


def TSP(G):
    return 0

def longest_path(G):
    
    return 0

def main():
    Vnum, Enum = input().split()
    graph = {}
    
    for _ in range (Vnum):
        v, u, w = input().split()
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v, w)
        graph[v].add(u, w)        

    print(graph)
    
    pass

if __name__ == "__main__":
    main()
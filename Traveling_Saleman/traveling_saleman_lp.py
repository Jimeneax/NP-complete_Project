"""
    name:  Alberto Jimenez Aaron Nyaanga

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
            https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/  
           TSP and LP solutions we referenced GeeksforGeeks
"""

from itertools import permutations

def calculate_path_length(path, graph):
    length = 0
    for i in range(len(path) - 1):
        if path[i + 1] in graph[path[i]]:
            length += graph[path[i]][path[i + 1]]
        else:
            # If the edge doesn't exist, break the loop
            length = float('-inf')
            break
    return length

def lp(graph):
    nodes = list(graph.keys())
    longest_path = None
    max_length = float('-inf')

    for p in permutations(nodes):
        length = calculate_path_length(p, graph)
        if length > max_length:
            max_length = length
            longest_path = p

    return max_length, longest_path

def main():
    n, m = map(int, input().split())
    graph = {chr(ord('a') + i): {} for i in range(n)}

    for _ in range(m):
        u, v, w = input().split()
        graph[u][v] = int(w)

    max_length, longest_path = lp(graph)

    if max_length == float('-inf'):
        print("No valid path exists.")
    else:
        print(max_length)
        print(" ".join(longest_path))

if __name__ == "__main__":
    main()

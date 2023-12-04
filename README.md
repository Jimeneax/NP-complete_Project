# NP-complete_Project
This project will explore an known NP-complete problem and will consist of the following components: Problem presentation explaining the problem to be solved and its reduction to another accepted NP-complete problem. Solution Code. Approximation presentation. Approximation code.

# Weighted Graph Problems (TSP, Longest Path)

The input is a weighted graph specified by a line containing the number of vertices n and the number of edges m followed by m lines containing the edges given in u v w format, representing an edge between u and v of weight w. TSP graphs are undirected and edges will be listed only once and the graph will be a complete graph. LP graphs are directed.

The output contains two lines: the length of the path on one line (as an integer) followed by a list of vertices for the path/cycle on the second line.

Example TSP input:

3 3
a b 3
b c 4
a c 5

Example TSP output:

12
a b c a

Example LP input:

3 3
a b 3
b c 4
a c 5

Example LP output:

7
a b c

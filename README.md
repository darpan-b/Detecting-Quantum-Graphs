# Detecting-Quantum-Graphs

Given a _connected, undirected, non-trivial, non-isomorphic to K4_ graph G=(V, E), this program does the following:
- Finds a matching covered graph G'=(V, E') in G.
- Checks whether G' is a connected or not. If G' is connected, it checks whether G' is a 2-connected or 3-connected graph.
- Checks whether G' is a Type-2 graph or not.

To check whether G' is a Type-2 graph or not, it rougly follows **Algorithm 1** in [Perfect Matchings and Quantum Physics: Progress on Krenn's Conjencture by L. Sunil Chandran and Rishikesh Gajjala](/2202.05562.pdf).

The graph G is provided input to the program in the following format:
```
Number of vertices in the graph: <insert |V| here>
Number of edges in the graph: <insert |E| here>
Edges of the graph (1-indexed): <insert all unordered pairs (u,v) in E here>
```

Plese check [Sample Testcases](/sample_testcases.txt) to gain a better understanding of the input / output format.

To run the program, please use **Python3**.
The command to run the program is:
`python "algo1_and_type_k.py"`.

Feel free to report any bugs / issues found.

-- Darpan

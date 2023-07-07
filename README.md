# Detecting-Quantum-Graphs

We give a program to rule out the counter examples for the [Krenn-Gu conjecture](https://mariokrenn.wordpress.com/graph-theory-question/).

From prior work, it is known that counter example cannot be a Type-2 graph [CG 22](/2022.05562.pdf). We roughly implement the Type-2 graph detection algorithm from [CG 22](/2022.05562.pdf) to detect such graphs. We also detect 2-connected graphs, which can not be a counter example and 3-connected graphs which can not be a minimal counter example. 

The graph G is provided input to the program in the following format:
```
Number of vertices in the graph: <insert |V| here>
Number of edges in the graph: <insert |E| here>
Edges of the graph (1-indexed): <insert all unordered pairs (u,v) in E here>
```

Plese check [Sample Testcases](/sample_testcases.txt) to gain a better understanding of the input / output format.

To run the program, please use **Python3**.
The command to run the program is:
`python "detecting_quantum_graphs.py"`.

Feel free to report any bugs / issues found.

-- Darpan

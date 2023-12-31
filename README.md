# Detecting-Quantum-Graphs

We give a program to rule out some large classes of graphs which cannot be the counter examples for the [Krenn-Gu conjecture](https://mariokrenn.wordpress.com/graph-theory-question/).

From prior work, it is known that counter example cannot be a Type-2 graph [[CG 22]](/2202.05562.pdf). We roughly implement the Type-2 graph detection algorithm from [[CG 22]](/2202.05562.pdf) to detect such graphs. We also detect 2-connected graphs, which can not be a counter example and 3-connected graphs which can not be a minimal counter example. 

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

For any queries or for reporting any bugs / issues, reader can mail at [dbhattacharya170803@gmail.com](mailto:dbhattacharya170803@gmail.com).

### References
[CG 22] L. S. Chandran and R. Gajjala. Perfect matchings and quantum physics: Progress on Krenn’s Conjecture, 2022.

---
#### Update (13.09.2023):
Commented and slightly restructured [/detecting_quantum_graphs.py](/detecting_quantum_graphs.py) to make it more readable. Added a function 'chandran_gajjala_is_type2()' which returns True if G is Type 2, otherwise returns False. Additionally, if G is not Type 2, the potential cause for it is now stated in the output.
[Sample Testcases](/sample_testcases.txt) updated accordingly.

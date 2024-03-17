# Ford-Fulkerson Algorithm Project

This project implements the Ford-Fulkerson algorithm to find the maximum flow through a network graph. The algorithm identifies augmenting paths and iteratively increases the flow until no more augmenting paths are found.

## Overview

The Ford-Fulkerson algorithm is used to compute the maximum flow in a flow network. It operates by finding augmenting paths from the entry to the exit and increasing the flow along these paths until no further augmenting paths can be identified.

## Implementation Details

The project is primarily composed of two functions:

- `bfs(residual_graph, entry, exit, parent)`: This function uses breadth-first search to find an augmenting path in the residual graph. It returns a boolean indicating whether a path to the exit node was found and also updates the `parent` list to store the path.
- `ford_fulkerson(graph, entry, exit)`: This function applies the Ford-Fulkerson algorithm using the `bfs` function to find augmenting paths and calculate the maximum flow from the `entry` to the `exit`.

The algorithm proceeds with the following steps, clearly annotated in the code:

1. Initialize a residual graph with the same capacities as the original graph.
2. Perform a BFS to locate an augmenting path in the residual graph.
3. Determine the minimum capacity along the discovered path.
4. Simulate the flow by the minimum capacity found in step 3.
5. Update the residual graph capacities and add reverse edges as needed.
6. Repeat steps 2-5 until no more augmenting paths can be found.
7. Return the calculated maximum flow.

## Expected Output
<img width="1512" alt="Screenshot 2024-03-17 at 12 26 06 AM" src="https://github.com/karamkhan1/Flows-and-Cuts/assets/79159011/251d58d5-a510-47e9-a1e6-f0b9a34561a5">
The maximum flow from entry (A) to exit (E) is: `11`

## Usage

To execute the algorithm, define a graph as an adjacency matrix where each element represents the capacity of an edge between nodes. Then, run the `ford_fulkerson` function with the entry and exit node indices.

```python
G = [
    [0, 20, 0, 0, 0],  # A
    [0, 0, 5, 6, 0],   # B
    [0, 0, 0, 3, 7],   # C
    [0, 0, 0, 0, 8],   # D
    [0, 0, 0, 0, 0]    # E
]

entry = 0  # Entry Node A
exit = 4   # Exit Node E

max_flow_value = ford_fulkerson(G, entry, exit)
print(f"The maximum flow from entry (A) to exit (E) is: {max_flow_value}")


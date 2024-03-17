from collections import deque


# Function to perform BFS on the graph from entry s to exit t
# It also fills parent[] to store the path
def bfs(residual_graph, s, t, parent):
    visited = [False] * len(residual_graph)
    queue = deque()
    queue.append(s)
    visited[s] = True

    # BFS loop [Step 2]
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(residual_graph[u]):
            if visited[ind] == False and val > 0:
                # If we find a connection to the exit t, then there is no point in BFS anymore
                # We just set its parent and can return true
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    # Path found
                    return True
    # We didn't reach exit t in BFS starting from entry s, so return false
    return False


# Ford-Fulkerson algorithm
def ford_fulkerson(graph, entry, exit):
    # This array is filled by BFS and to store path
    parent = [-1] * len(graph)

    # There is no flow initially
    max_flow = 0

    # Simulate the flow while there is a path from the entry to exit
    # The residual graph is modified by BFS, which is why we pass graph as an argument
    # Step 1: Initialize residual graph with the same capacities as the original graph
    residual_graph = [row[:] for row in graph]  # Create a copy of the graph for residual capacities
    while bfs(residual_graph, entry, exit, parent):

        # Step 3: find the minimum capacity along the found path
        path_flow = float('inf')
        s = exit
        while (s != entry):
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Step 4: add the minimum capacity (path flow) to the total max flow
        max_flow += path_flow

        # Step 5: update residual graph capacities and reverse edges along the path
        v = exit
        while (v != entry):
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    # Step 6: return the maximum flow after no path can be found anymore
    return max_flow


# Test graph, expect max flow = 11
G = [
    [0, 20, 0, 0, 0],  # A
    [0, 0, 5, 6, 0],  # B
    [0, 0, 0, 3, 7],  # C
    [0, 0, 0, 0, 8],  # D
    [0, 0, 0, 0, 0]  # E
]

entry = 0  # Node A
exit = 4  # Node E

max_flow_value = ford_fulkerson(G, entry, exit)
print(f"The maximum flow from entry (A) to exit (E) is: {max_flow_value}")

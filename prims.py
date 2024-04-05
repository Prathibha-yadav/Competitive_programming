from collections import  defaultdict
from heapq import heappush, heappop

def prims(graph, start):
    visited = []
    q = []
    weights = {}
    for vertex in graph:
        weights[vertex] = float('inf')
    weights[start] = 0
    parents = {}
    heappush(q, (0, start))

    while len(q) != 0:
        cur_wt, cur_vtx = heappop(q)

        for weight, node in graph[cur_vtx]:
            if node not in visited and weight < weights[node]:
                weights[node] = weight
                parents[node] = cur_vtx
                heappush(q, (weight, node))
        visited.append(cur_vtx)
    print(parents)
    print(weights)

graph = {
    "A": [(1,"B"), (3, "E")],
    "B": [(1, "A"), (4, "C"), (1, "D"), (2, "E")],
    "C": [(4, "B"), (1, "D")],
    "D": [(1, "B"), (1, "C"), (2, "E")],
    "E": [(3, "A"), (2, "B"), (2, "D")]
}
mst = prims(graph, "A")
print(mst)

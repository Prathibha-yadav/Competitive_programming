graph = {"A": ["B","E"],
         "B": ["A","C","D","E"],
         "C": ["B","D"],
         "D": ["B","C","E"],
         "E": ["A","B","D"]
        }

def bfs(graph,vertex):
        visited = [vertex]
        q = [vertex]
        while len(q) != 0 :
            ele = q.pop(0)
            for vxt in graph[ele]:
                if vxt not in visited:
                    visited.append(vxt)
                    q.append(vxt)
        return visited
             
opt = bfs(graph, "D")
print(opt)
     
     
                                                     

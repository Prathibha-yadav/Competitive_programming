graph = {"A": ["B","E"],
         "B": ["A","C","D","E"],
         "C": ["B","D"],
         "D": ["B","C","E"],
         "E": ["A","B","D"]
        }

def dfs(graph,start, visited = []):
        if(len(visited) == 0):
            visited.append(start)
            for vxt in graph[start]:
                if vxt not in visited:
                    visited.append(vxt)
                    dfs(graph, vxt, visited)
                    
        return visited
             
opt = dfs(graph, "B")
print(opt)
     
     
                                                     

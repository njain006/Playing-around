def dfs(graph, start):
    visited, stack = set(), [start]
    print ("Start",[start])
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print ("Vertex",vertex)
            print ("graph",graph[vertex])
            stack.extend(graph[vertex] - visited)
            print ("Visited",visited)
    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
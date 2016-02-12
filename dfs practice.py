def dfs(graph,start):
	visited, stack = set(), [start]
	print ("Visited",visited)
	print ("stack",stack)
	while stack:
		vertex = stack.pop()
		print ("Vertex",vertex)
		if vertex not in visited:
			
			visited.add(vertex)
			stack.extend(graph[vertex]-visited)
			print ("stack",stack)
	return visited
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

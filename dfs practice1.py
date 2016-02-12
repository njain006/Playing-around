def iterative_dfs(graph,start,path=[]):
	q = [start]
	while q:
		visited = q.pop()
		if visited not in path:
			path=path+[visited]
			q = graph[visited]+q
	return path

def iterative_bfs(graph,start,path=[]):
	q=[start]
	while q:
		visited = q.pop(0)
		print ("visited",visited)
		if  visited not in path:
			path = path +[visited]
			q = q+graph[visited]
	return path			

def rec_dfs(graph,start,path=[]):
	q=[start]
	visited = q.pop()
	if visited not in path:
		path = path + [visited]
		q=graph[visited]+q
	return print(rec_dfs(graph,visited))

graph = {'A':['B','C'],
         'B':['D','E'],
         'C':['D','E'],
         'D':['E'],
         'E':['A']}
print ('iterative dfs ', iterative_dfs(graph, 'E'))
print ('iterative bfs ', iterative_bfs(graph, 'E'))
print ('recursive dfs ', rec_dfs(graph, 'E'))
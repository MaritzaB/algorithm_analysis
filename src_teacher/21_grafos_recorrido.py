
graph = {
  'A' : ['B','C'],
  'B' : ['D','E','A'],
  'C' : ['F','G','A'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : []
}

def bfs(graph, node):
  queue = []
  expand=[]
  visited = []
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    expand.append(s)
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return expand
 
def dfs(graph, node):
    if node not in visited:
        expan.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)
   
        
expan=[]
visited=set()                  
bfs(graph,'A') 
dfs(graph,'A')  
      


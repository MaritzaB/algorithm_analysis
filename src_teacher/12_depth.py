# Using a Python dictionary to act as an adjacency list
graph2 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
graph1 = {
  'A' : ['B','C'],
  'B' : ['D','E'],
  'C' : ['F','G'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : []
}


graph = {
    'A' : ['B','C'],
    'B' : ['A', 'C'],
    'C' : ['A','B','D'],
    'D' : ['C','E','F','G'],
    'E' : ['F','G'],
    'F' : ['D','E'],
    'G' : ['D','E']
}

import networkx as nx
import matplotlib.pyplot as plt

nx.draw_networkx(g, node_color='green', node_size=700)
g = nx.Graph()
g.add_edges_from([(3, 4), (5, 6)])

visited = set() 
expand=[]

def dfs(graph, node):
    if node not in visited:
        expand.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)

# Driver Code
dfs(graph1, 'A')
root=('A','A')
dfs_tree(graph1, root)


def dfs_tree(graph, node_item):
    (node,nodep)=node_item
    if node not in visited:
        print (node)
        visited.add(node)
        if node != nodep:
          print (node_item)
          edges_tree.append(node_item)
        for neighbour in graph[node]:
            node_item=(neighbour,node)
            dfs_tree(graph, node_item)
            
            


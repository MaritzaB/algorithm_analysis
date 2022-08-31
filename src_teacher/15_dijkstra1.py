
import networkx as nx
import matplotlib.pyplot as plt
edgw=edgesw(graph)
G=nx.Graph()
G.add_weighted_edges_from(edgw)
draw_graphw(G)

def draw_graphw(G):
  nx.draw(G, pos=pos, node_color='r', node_size=250, with_labels=True)
  labels = nx.get_edge_attributes(G,'weight')
  nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
  return plt.show()
  
def edgesw(g):
  edg = []
  for u in g:
    for v in g[u]:
      if ((u,v,g[u][v]) not in edg) and ((v,u,g[v][u]) not in edg):
        edg.append((u, v,g[u][v]))
  return edg
 
 
  
nx.dijkstra_path(g, 1, 2,weight="weight")
nx.dijkstra_path_length(g, 1, 2,weight="weight")
g.add_weighted_edges_from(edgw)
edgw=edgesw(graph1)
 g = nx.Graph()


from numpy import inf

graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 'B': {'H': 1, 'G': 3}, 'C': {'I': 2, 'D': 3, 'A': 5},
         'D': {'C': 3, 'A': 1, 'H': 2}, 'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1}, 'G': {'F': 1, 'B': 3, 'H': 2}, 'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
         'I': {'C': 2, 'H': 2}}
         
         
graph1 = {1: {3: 5, 4: 1, 5: 2}, 2: {8: 1, 7: 3}, 3: {9: 2, 4: 3, 1: 5},
         4: {3: 3, 1: 1, 8: 2}, 5: {1: 2, 6: 3},
         6: {5: 3, 7: 1}, 7: {6: 1, 2: 3, 8: 2}, 8: {9: 2, 4: 2, 2: 1, 7: 2},
         9: {3: 2, 8: 2}}
         
costs = {1: 0, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf, 7: inf, 8: inf, 9: inf}      

costs1 = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf}


def search(source, target, graph, costs):
    
    parents = {}
    nextNode = source
    
    while nextNode != target:
        
        for neighbor in graph[nextNode]:
            
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                
                parents[neighbor] = nextNode
                
            del graph[neighbor][nextNode]
            
        del costs[nextNode]
        
        nextNode = min(costs, key=costs.get)
    path=back(source,target,parents)
        
    return path,costs[target] 

result = search('A', 'B', graph, costs)

def back(source, target, searchResult):
    
    node = target
    
    backpath = [target]
    
    path = []
    
    while node != source:
        
        backpath.append(searchResult[node])
        
        node = searchResult[node]
        
    for i in range(len(backpath)):
        
        path.append(backpath[-i - 1])
        
    return path





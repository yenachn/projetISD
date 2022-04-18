#redefine coordinate weights
def dist(tup1, tup2):
  return ((tup1[0]-tup2[0])**2+(tup1[1]-tup2[1])**2 + (tup1[2]-tup2[2])**2 + 1.5*(tup1[3]-tup2[3])**2 + 1.5*(tup1[4]-tup2[4])**2)**(1/2)

#define epsilon, to hand tune later
eps = 0

def graph(arr):
  res = {}
  for i in range(len(arr)):
    neighbors = []
    for j in range(len(arr)):
      if i !=j and dist(arr[i], arr[j]) <= eps:
        neighbors.append(arr[j])
    res[arr[i]] = neighbors
  return res

def crop_outl(graph):
  for key in graph:
    if len(graph[key])==0:
      graph.pop(key)

def parcourir(graph, node, cluster, visited):
  neighbor_indices = graph[node]
  for neighbor_node in neighbor_indices:
    if not visited[neighbor_node]:
      visited[neighbor_node] = True
      cluster.append(neighbor_node)
      parcourir(graph, neighbor_node, cluster, visited)

def cluster(graph, node, visited):
  cluster = []
  parcourir(graph, node, cluster, visited)
  return cluster

def cluster_size(cluster):
  return cluster.length()

def clusters(graph):
  clusters = []
  visited = {}
  for key in graph:
    visited[key] = False
  for key in visited:
    if not visited[key]:
      clusters.append(cluster(graph, key, visited))
  return clusters


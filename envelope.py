# convex envelope of the clusters

def slopesort(cluster, graph, p):
  slopes = {}
  neighbor_indices = graph[p]
  for neighbor_index in neighbor_indices:
    neighbor_node = graph[neighbor_index]
    if p[3] == neighbor_node[3]:
      slopes.append[float('inf')] = neighbor_node
    else:
      slopes.append[1.0*(p[4]-neighbor_node[4])/(p[3]-neighbor_node[3])]
  return slopes 

def rotation_left(p1, p2, p3):
  return not ((p2[3] - p1[3])*(p3[4] - p1[4])) - ((p2[4] - p1[4])*(p3[3] - p1[3]) < 0)

def envelope(cluster, graph):
  envelope = []
  p_ = cluster[0]
  for point in cluster:
    if point[4] < p_[4] or (point[4] == p_[4] and point[3] < p_[3]):
      p_ = point
  envelope.append(p_)
  for i in range(2):
    slopes = slopesort(cluster, graph, envelope[i])
    envelope.append(slopes[list(slopes.keys()).sort()[0]])
  while not envelope[-1] == p_:
    slopes = slopesort(cluster, graph, envelope[-1])
    envelope.append(slopes[list(slopes.keys()).sort()[0]])
    while len(envelope)>2 and not rotation_left(envelope[-1], envelope[-2], envelope[-3]):
      envelope.remove(envelope[-2])
  return envelope

def envelopes(clusters, graph):
  envelopes = []
  for cluster in clusters:
    envelopes.append(envelope(cluster))
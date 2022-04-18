from envelope import *
from clusters import *
import math as m

def circular(cluster, envelope):
    return m.pi * (max_length(envelope)/2)**2 / cluster_size(cluster)

def minmax_ratio(envelope):
  max, min = (envelope[0], envelope[1], distance(envelope[0], envelope[1]))
  for vertice in envelope:
    for another_vertice in envelope:
      if distance(vertice, another_vertice) > max[2]:
        max = (vertice, another_vertice, distance(vertice, another_vertice))
      elif distance(vertice, another_vertice) < min[2]:
        min = (vertice, another_vertice, distance(vertice, another_vertice))
  return min/max


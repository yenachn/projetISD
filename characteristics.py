from envelope import *
from clusters import *
import math as m

# ratio between actual size and assumed circular form
# use for: find hyperplane divising the ratios of circular and noncircular
def circular(cluster, envelope):
    return m.pi * (max_length(envelope)/2)**2 / cluster_size(cluster)

# ratio between shortest and longest distance
# use for: find hyperplane divising the ratios of rectangular gelules and circular pilules, evidently rectangular gelules have significantly greater ratios
# important: halved gelules will have a visibly smaller ratio than complete gelules, and a visibly bigger one than circular pills. two times binary classification
def minmax_ratio(envelope):
  max, min = (envelope[0], envelope[1], distance(envelope[0], envelope[1]))
  for vertice in envelope:
    for another_vertice in envelope:
      if distance(vertice, another_vertice) > max[2]:
        max = (vertice, another_vertice, distance(vertice, another_vertice))
      elif distance(vertice, another_vertice) < min[2]:
        min = (vertice, another_vertice, distance(vertice, another_vertice))
  return min/max


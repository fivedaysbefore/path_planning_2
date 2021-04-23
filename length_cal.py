# five days before
# 时间 2021/4/2 10:36
from main import dict_net_node_coordinate as nodes
from main import list_net_edges as edges
from main import path_info
import numpy
import xlwt
#def length_calculate(nodes, edges):
path_length = []
for edge in range(len(edges)):
    point_start = edges[edge][0]
    point_end = edges[edge][1]
    edge_length = numpy.sqrt((nodes[point_end][0]-nodes[point_start][0])**2 +\
                  (nodes[point_end][1]-nodes[point_start][1])**2)
    path_length.append(round(edge_length, 0))
print(path_length)

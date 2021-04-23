# five days before
# 时间 2021/4/9 20:33
import numpy

"""一次获得一个h矩阵即可，可多次调用"""
"""此函数用来获得路径规划的启发函数"""


def get_hn(point_start, list_end_point, list_disabled_point, dict_net_node_coordinate,
           list_net_nodes):
    nodes = dict_net_node_coordinate
    point_distance = []
    hn_1 = []
    hn_2 = []
    max_num = 100_000_000
    """某点不可用时定义启发值巨大"""
    """首先为起点寻找最近的终点"""
    for j in range(len(list_end_point)):
        point_end = list_end_point[j]
        distance = numpy.sqrt((nodes[point_end][0] - nodes[point_start][0]) ** 2 + \
                              (nodes[point_end][1] - nodes[point_start][1]) ** 2)
        point_distance.append(distance)
    """排序得到距离最小值和次小值的索引"""
    point_distance_2 = sorted(list(set(point_distance)))
    for i, k in enumerate(point_distance):
        if point_distance[i] < point_distance_2[1]:
            best_end_point = list_end_point[i]
        elif point_distance[i] == point_distance_2[1]:
            second_end_point = list_end_point[i]
    """起点与终点一一对应，可开始构造启发函数的矩阵"""
    """先获得第一出口的hn"""
    nodes_num = len(list_net_nodes)
    for node in range(1, nodes_num + 1):
        if node == best_end_point:
            hn_1.append(0)
        elif node in list_disabled_point:
            hn_1.append(max_num)
        else:
            length_hn_1 = int(numpy.sqrt((nodes[best_end_point][0] - nodes[node][0]) ** 2 + \
                                         ((nodes[best_end_point][1] - nodes[node][1]) ** 2)))
            hn_1.append(length_hn_1)
    """获得第二出口的hn"""
    for node in range(1, nodes_num + 1):
        if node == second_end_point:
            hn_2.append(0)
        elif node in list_disabled_point:
            hn_2.append(max_num)
        else:
            length_hn_2 = int(numpy.sqrt((nodes[second_end_point][0] - nodes[node][0]) ** 2 + \
                                         ((nodes[second_end_point][1] - nodes[node][1]) ** 2)))
            hn_2.append(length_hn_2)
    return hn_1, best_end_point, hn_2, second_end_point

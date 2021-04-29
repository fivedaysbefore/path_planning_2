# five days before
# 时间 2021/3/28 17:21
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Circle
import numpy as np

import map_data_read
import map_information
import point_set
import get_h
import path_planning_Astar
import get_init_graph
import get_map
import get_now_graph
import draw_path
import path_planning_dijkstra
import get_density
import path_select
import fire_diffusion
import test_path
length_final = 0
length_final, length_next, length_last = 0, 0, 0
"""读取轮船地图信息"""
data_path = "C:\\Users\\five days before\\Desktop\\毕业设计\\文档\\point_position.xlsx"
path_info = "C:\\Users\\five days before\\Desktop\\毕业设计\\文档\\adj_list.xlsx"
point_set_info = "C:\\Users\\five days before\\Desktop\\毕业设计\\文档\\point_set_info.xlsx"
"""调用信息获取函数，对路径信息进行存储"""
dict_path_info = map_information.map_information(path_info)
# print(dict_path_info)
"""调用绘图函数进行地图绘制"""
dict_net_node_coordinate, path_info_data, list_net_edges, list_net_nodes = \
    map_data_read.map_draw(data_path, path_info)
# print('path_info_data:', path_info_data)
# print('dict_net_node_coordinate:', dict_net_node_coordinate)
# print(list_net_edges, list_net_nodes, sep='\n')
"""调用point_set函数，得到终点、起点、不可用点、不可用路径"""
"""得到point_set函数的返回值，包括终点、起点、不可用点、不可用路径"""
list_start_point, list_end_point, list_disabled_point, list_disabled_path, list_crowd_density \
    = point_set.point_set(point_set_info)

i = 0
dict_edge_density = {}
list_before_point = []

for point in list_start_point:
    edge_density = {(0,point): list_crowd_density[i]}
    dict_edge_density.update(edge_density)
    i += 1

for edge in list_net_edges:
    edge_density = {edge: 0}
    dict_edge_density.update(edge_density)

fire_time = 0
list_start_point_now = list(list_start_point)

while fire_time < 50:
    map_data_read.map_draw(data_path, path_info)
    list_disabled_point_now, list_disabled_path_now = fire_diffusion.fire_diffusion(list_disabled_point,
                                                                                    list_disabled_path,
                                                                                    dict_net_node_coordinate,
                                                                                    list_net_edges, fire_time)
    print('\n火灾时间：', fire_time)
    print('不可用点：', list_disabled_point_now, '不可用路径:', list_disabled_path_now)
    # print(list_crowd_density)
    # print(list_start_point, list_end_point, list_disabled_point, list_disabled_path, sep='\n')

    """得到排除不可用情况后的绘图信息"""
    list_net_edges_now, list_net_nodes_now, dict_nodes_labels_now, dict_net_node_coordinate_now, nodes_NUM = \
        get_now_graph.get_now_graph(list_disabled_point_now, list_disabled_path_now,
                                    list_net_edges, list_net_nodes, dict_net_node_coordinate)
    """得到路径规划信息graph, list_dijk_edges """
    graph, list_dijk_edges = get_init_graph.init_graph(nodes_NUM, path_info_data, list_net_edges_now)
    """绘制不可用信息引入后的地图"""
    get_map.get_map_now(list_net_edges_now, list_net_nodes_now, dict_nodes_labels_now, dict_net_node_coordinate_now)
    list_end_point_used = []
    all_path = []
    all_cost = []
    # """对所有节点进行路径规划"""
    # """出口数大于等于2"""
    if len(list_end_point) > 1:
        for i in range(len(list_start_point_now)):
            start_point = list_start_point_now[i]
            h1, end_point, h2, end_point_2 = get_h.get_hn(start_point, list_end_point, list_disabled_point_now,
                                                          dict_net_node_coordinate,
                                                          list_net_nodes)
            # print(h, start_point, end_point, sep= '\n')
            """A*算法"""
            # cost_1, path_1 = path_planning_Astar.astar_path_finding(graph, nodes_NUM, start_point, end_point, h1)
            """Dijkstra算法"""
            cost_1, path_1 = path_planning_dijkstra.dijkstra_path_planning(list_dijk_edges, start_point, end_point)
            """为什么不把相同算法放在一起，因为需要只获得最优出口的使用情况"""
            if end_point not in list_end_point_used:
                list_end_point_used.append(end_point)
            """A*算法"""
            # cost_2, path_2 = path_planning_Astar.astar_path_finding(graph, nodes_NUM, start_point, end_point_2, h2)
            """Dijkstra算法"""
            cost_2, path_2 = path_planning_dijkstra.dijkstra_path_planning(list_dijk_edges, start_point, end_point_2)
            all_path.append(path_1)
            all_path.append(path_2)
            all_cost.append(cost_1)
            all_cost.append(cost_2)
        dict_crowd_density_now = get_density.now_crowd_density(list_end_point_used, list_crowd_density)
        #print('出口人数：', dict_crowd_density_now)
        all_path_now, all_cost_now = path_select.all_path_select(all_path, all_cost, dict_crowd_density_now)
        # print('all_path_now:',all_path_now)
        for path in all_path_now:
            draw_path.draw_path_now(path, dict_net_node_coordinate)
    else:
        for i in range(len(list_start_point_now)):
            start_point = list_start_point[i]
            end_point = list_end_point[0]
            cost_1, path_1 = path_planning_dijkstra.dijkstra_path_planning(list_dijk_edges, start_point, end_point)
            all_path.append(path_1)
        for path in all_path:
            draw_path.draw_path_now(path, dict_net_node_coordinate)

    list_start_point_now, dict_edge_density, length_final = test_path.path_update(all_path_now,list_start_point,length_final,dict_edge_density,
                                                list_dijk_edges, fire_time)
    for key in dict_edge_density:
        if dict_edge_density[key]:
            print('人流密度：', key,":", dict_edge_density[key])
            # print('list_start_point_now:',list_start_point_now)
    fire_time += 10
# """标注"""
# plt.text(170, 65, 'start', fontsize=5, backgroundcolor='red', alpha=0.6)
# plt.text(190, 65, 'end', fontsize=5, backgroundcolor='maroon', alpha=0.6)
# plt.text(210, 65, 'disabled', fontsize=5, backgroundcolor='gray', alpha=0.6)
# plt.text(240, 65, 'path', fontsize=5, backgroundcolor='orange', alpha=0.6)
# plt.axis('equal')
# plt.show()

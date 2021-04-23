# five days before
# 时间 2021/3/26 22:27

import networkx as nx
import matplotlib.pyplot as plt
import xlrd


def map_draw(data_path, path_info):
    """"读取节点坐标文件"""
    # data_path = "C:\\Users\\five days before\\Desktop\\毕业设计\\文档\\point_position.xlsx"
    book_1 = xlrd.open_workbook(data_path)
    point_position = book_1.sheets()[0]
    nrows_1 = point_position.nrows
    list_path_position_data = []
    list_net_nodes = []
    dict_net_node_coordinate = {}
    """" 用dict_net_node_coordinate来存储节点、坐标信息"""
    for row in range(1, nrows_1):
        list_path_position_data.append(point_position.row_values(row))
        point_number = int(list_path_position_data[row - 1][0])
        list_net_nodes.append(point_number)
        point_value = tuple(list_path_position_data[row - 1][1:3])
        dict2 = {point_number: point_value}
        """dict_net_node_coordinate：路径节点信息，字典方式，key为节点号，value为对应坐标"""
        dict_net_node_coordinate.update(dict2)

    """读取路径信息"""

    #path_info = "C:\\Users\\five days before\\Desktop\\毕业设计\\文档\\adj_list.xlsx"
    book_2 = xlrd.open_workbook(path_info)
    path_information = book_2.sheets()[0]
    nrows_2 = path_information.nrows
    """获取路径信息文件的列数"""
    # ncols_2 = path_information.ncols
    path_info_data = []
    list_net_edges = []
    """list_net_edges:元素为元组，表示该路径的起点和终点"""
    for row in range(1, nrows_2):
        path_info_data.append(path_information.row_values(row))
        path_connect = tuple(list(map(int, path_info_data[row - 1][0:2])))
        list_net_edges.append(path_connect)
    #print(dict_net_node_coordinate, path_info_data, list_net_edges, list_net_nodes,sep='\n')

    net_grid = nx.Graph()

    dict_nodes_labels = dict(zip(list_net_nodes, list_net_nodes))

    net_grid.add_nodes_from(list_net_nodes)
    net_grid.add_edges_from(list_net_edges)

    """ 画图"""
    nx.draw_networkx_nodes(net_grid, dict_net_node_coordinate, list_net_nodes, node_size=50, node_color='gray')
    nx.draw_networkx_edges(net_grid, dict_net_node_coordinate, list_net_edges, edge_color="gray")
    nx.draw_networkx_labels(net_grid, dict_net_node_coordinate, dict_nodes_labels, 5)

    return dict_net_node_coordinate, path_info_data, list_net_edges, list_net_nodes
    # plt.show()

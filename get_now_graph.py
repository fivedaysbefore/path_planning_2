# five days before
# 时间 2021/4/4 12:20
def get_now_graph(list_disabled_point, list_disabled_path,
                  list_net_edges, list_net_nodes, dict_net_node_coordinate):
    nodes_NUM = len(list_net_nodes)- len(list_disabled_point)
    list_net_edges_now = []
    list_net_nodes_now = []
    dict_net_node_coordinate_now = dict_net_node_coordinate

    for key in list_disabled_point:
        del dict_net_node_coordinate_now[key]

    for net_node in list_net_nodes:
        if net_node not in list_disabled_point:
            list_net_nodes_now.append(net_node)

    for net_edges in list_net_edges:
        if net_edges not in list_disabled_path:
            list_net_edges_now.append(net_edges)
    length_edge = len(list_net_edges_now)
    for i in range(length_edge - 1, -1, -1):
        for j in range(2):
            if list_net_edges_now[i][j] in list_disabled_point:
                del list_net_edges_now[i]

    dict_nodes_labels_now = dict(zip(list_net_nodes_now, list_net_nodes_now))
    # '''测试'''
    # print('list_net_edges_now:', list_net_edges_now)
    return list_net_edges_now, list_net_nodes_now, dict_nodes_labels_now, dict_net_node_coordinate_now, nodes_NUM
# five days before
# 时间 2021/4/4 19:51
import networkx as nx


def draw_path_now(path, dict_net_node_coordinate):
    net_grid = nx.Graph()
    list_edges = []
    path_num = len(path)
    start_node = [0]
    end_node = [0]
    start_node[0] = path[0]
    end_node[0] = path[path_num - 1]
    for i in range(path_num - 2, -1, -1):
        edge = tuple(path[i:i + 2])
        list_edges.append(edge)
    net_grid.add_nodes_from(path)
    net_grid.add_edges_from(list_edges)
    nx.draw_networkx_nodes(net_grid, dict_net_node_coordinate, end_node, node_size=50, node_color='maroon')
    nx.draw_networkx_nodes(net_grid, dict_net_node_coordinate, start_node, node_size=50, node_color='red')
    nx.draw_networkx_edges(net_grid, dict_net_node_coordinate, list_edges, edge_color='orange')

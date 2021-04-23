# five days before
# 时间 2021/4/4 11:45
import networkx as nx
def get_map_now(list_net_edges_now, list_net_nodes_now, dict_nodes_labels_now,dict_net_node_coordinate_now):
    net_grid = nx.Graph()
    net_grid.add_nodes_from(list_net_nodes_now)
    net_grid.add_edges_from(list_net_edges_now)
    """ 画图"""
    nx.draw_networkx_nodes(net_grid, dict_net_node_coordinate_now, list_net_nodes_now, node_size=50)
    nx.draw_networkx_edges(net_grid, dict_net_node_coordinate_now, list_net_edges_now, edge_color="k")
    nx.draw_networkx_labels(net_grid, dict_net_node_coordinate_now, dict_nodes_labels_now, 5)

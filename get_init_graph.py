# five days before
# 时间 2021/4/3 16:26
import get_now_graph
"""通过对 point_set_info里的信息进行读取，更新路径规划所用的数据库"""
"""获得新的地图"""
def init_graph(nodes_NUM, path_info_data,list_net_edges_now):
    # 地图
    class Graph:
        def __init__(self):
            self.ship_graph = [[0] * nodes_NUM for i in range(nodes_NUM)]

        def add_edge(self, _from, _to, _value):
            if _from < nodes_NUM:
                if _to < nodes_NUM:
                    self.ship_graph[_from][_to] = _value
                    self.ship_graph[_to][_from] = _value

        def get_edge(self, _from, _to):
            return self.ship_graph[_from][_to]

    graph = Graph()
    list_dijk_edges = []
    """起点、终点、长度"""
    for i in range(len(list_net_edges_now)):
        for j in range(len(path_info_data)):
            if (int(path_info_data[j][0]) == list_net_edges_now[i][0]) and \
                (int(path_info_data[j][1]) == list_net_edges_now[i][1]):
                graph.add_edge(int(path_info_data[j][0]),
                               int(path_info_data[j][1]),
                               int(path_info_data[j][2]))
                list_dijk_edges.append((int(path_info_data[j][0]),
                               int(path_info_data[j][1]),
                               int(path_info_data[j][2])))
                list_dijk_edges.append((int(path_info_data[j][1]),
                               int(path_info_data[j][0]),
                               int(path_info_data[j][2])))
    #print('list_dijk_edges:',list_dijk_edges)
    return graph, list_dijk_edges
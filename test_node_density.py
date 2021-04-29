def node_density_update(all_path_now,
                list_start_point,
                list_before_point,
                dict_node_density,
                list_dijk_edges,
                fire_time):

    dict_edge_length = {}
    path_with_node = []
    people_speed = 1.7
    start_i = 0
    """dict_edge_length:{(node_pair):length}"""
    """得到每一条路径的长度"""
    for dijk_edge in list_dijk_edges:
        node_1 = (dijk_edge[0], dijk_edge[1])
        length_1 = dijk_edge[2]
        node_length = {node_1: length_1}
        dict_edge_length.update(node_length)

    for path in all_path_now:
        length_next = 0
        for i in range(len(path)-1):
            node_pair = (path[i], path[i+1])
            length_last = length_next
            length_next += dict_edge_length[node_pair]
            time_to_last = length_last / people_speed
            time_to_next = length_next / people_speed
            if fire_time <= time_to_next and fire_time > time_to_last:



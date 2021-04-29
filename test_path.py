global length_final, length_next, length_last
def path_update(all_path_now,
                list_start_point,
                length_final,
                dict_edge_density,
                list_dijk_edges,
                fire_time):

    list_start_point_now = []
    dict_edge_length = {}
    path_with_node = []
    people_speed = 1.7
    flag_find = 0
    """dict_edge_length:{(node_pair):length}"""
    """得到每一条路径的长度"""
    for dijk_edge in list_dijk_edges:
        node_1 = (dijk_edge[0], dijk_edge[1])
        length_1 = dijk_edge[2]
        node_length = {node_1: length_1}
        dict_edge_length.update(node_length)

    """path_with_node: [[(2,3),(3,4),(4,5)...],[...],[...]]"""
    for path in all_path_now:
        #print("路径起点：", path[0])
        path_with_point_temp = []
        if path[0] in list_start_point:
            dict_edge_density[(path[0], path[1])] = dict_edge_density[(0, path[0])]
            dict_edge_density[(0, path[0])] = 0
        for i in range(len(path) - 1):
            edge = (path[i], path[i + 1])
            path_with_point_temp.append(edge)
        path_with_node.append(path_with_point_temp)
    #print('path_with_node:', path_with_node)
    for path in path_with_node:
        length_next = length_final
        #length_last = 0
        for node_2 in path:
            # try:
            length_last = length_next
            length_next += dict_edge_length[node_2]
            # except KeyError:
            #     length_next = length_next
            time_to_next = length_next / people_speed
            time_to_last = length_last / people_speed
            # print('time_to_last:', time_to_last)
            # print('time_to_next:', time_to_next)
            if fire_time <= time_to_next and not fire_time <= time_to_last:
                print(22222)
                flag_find = 1
                length_final = length_next
                next_start = node_2[1]
                list_start_point_now.append(next_start)
                if node_2[0] > node_2[1]:
                    node_2 = (node_2[1], node_2[0])
                if path[0][0] > path[0][1]:
                    path[0] = (path[0][1], path[0][0])
                if node_2 != path[0]:
                    print(22333333)
                    dict_edge_density[node_2] += dict_edge_density[path[0]]
                    dict_edge_density[path[0]] = 0
                break
        if flag_find == 0:
            if path:
                length_final = length_final + dict_edge_length[path[0]]
                if path[0][1] not in list_start_point_now:
                    list_start_point_now.append(path[0][1])
            else:
                print("该起点已成功疏散")




    return list_start_point_now, dict_edge_density,length_final

import switch_element as se

def path_update(all_path_now,
                list_start_point,
                length_final,
                dict_edge_density,
                list_dijk_edges,
                fire_time):

    global fire_step
    fire_step = 10
    list_start_point_now = []
    dict_edge_length = {}
    path_with_node = []
    people_speed = 1
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
            path_with_point_temp = [(0, path[0])]
        for i in range(len(path) - 1):
            edge = (path[i], path[i+1])
            path_with_point_temp.append(edge)
        path_with_node.append(path_with_point_temp)
    # print('path_with_node:', path_with_node)

    for path in path_with_node:
        length_next = length_final
        #length_last = 0
        for node_2 in path:
            try:
                length_last = length_next
                length_next += dict_edge_length[node_2]
            except KeyError:
                length_last = length_next
                length_next = length_next
            time_to_next = length_next / people_speed
            time_to_last = length_last / people_speed
            # print('time_to_last:', int(time_to_last))
            # print('time_to_next:', int(time_to_next))
            # print('fire_time:', fire_time)
            if fire_time < time_to_next and not fire_time < time_to_last:
                flag_find = 1
                if fire_step+fire_time >= time_to_next:
                    length_final = length_next
                    next_start = node_2[1]
                    i = path.index(node_2)
                    # if next_start in list_end_point:
                    #     print('该点以成功疏散')
                    #break
                    if next_start not in list_start_point_now:
                        list_start_point_now.append(next_start)
                    node_2 = se.switch(node_2)
                    path[0] = se.switch(path[0])
                    if node_2 != path[0] :
                        if path[0][0] == 0:
                            try:
                                path[i+1] = se.switch(path[i+1])
                                path[1] = se.switch(path[1])
                                dict_edge_density[path[i+1]] += dict_edge_density[path[1]]
                                dict_edge_density[path[1]] = 0
                            except IndexError:
                                pass

                        else:
                            dict_edge_density[path[i+1]] += dict_edge_density[path[0]]
                            dict_edge_density[path[0]] = 0
                else:
                    length_final = length_last
                    next_start = node_2[0]
                    if next_start not in list_start_point_now:
                        list_start_point_now.append(next_start)
                    if node_2 != path[0]:
                        node_2 = se.switch(node_2)
                        path[0] = se.switch(path[0])
                        dict_edge_density[node_2] += dict_edge_density[path[0]]
                        dict_edge_density[path[0]] = 0
                break

        # if flag_find == 0:
        #     if path:
        #         path[0] = se.switch(path[0])
        #         path[1] = se.switch(path[1])
        #         time_to_second = dict_edge_length[path[0]] / people_speed
        #         if path[0][1] not in list_start_point_now and time_to_second <= fire_step:
        #             length_final = length_final + dict_edge_length[path[0]]
        #             list_start_point_now.append(path[0][1])
        #         elif path[0][0] not in list_start_point_now:
        #             length_final = length_final
        #             list_start_point_now.append(path[0][0])
        #         if len(path) > 1:
        #             dict_edge_density[path[1]] += dict_edge_density[path[0]]
        #             dict_edge_density[path[0]] = 0
        #         # else:
        #         #     dict_edge_density[path[0]] = 0
        #     else:
        #         print("该起点已成功疏散")


    for key in dict_edge_density:
        if dict_edge_density[key]:
            print('人流密度：', key, ":", dict_edge_density[key])
            # print('list_start_point_now:',list_start_point_now)
    return list_start_point_now, dict_edge_density,length_final

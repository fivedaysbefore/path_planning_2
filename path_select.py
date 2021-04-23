# five days before
# 时间 2021/4/10 19:44
import path_compare
def all_path_select(all_path, all_cost, dict_crowd_density_now):
    all_path_now = []
    all_cost_now = []
    length = len(all_path)-1
    for i in range(0, length, 2):
        target_end = all_path[i+1][-1]
        now_end = all_path[i][-1]
        if target_end not in dict_crowd_density_now:
            target_crowd_density = 0
            now_crowd_density = dict_crowd_density_now[now_end]
            path, cost = path_compare.path_compare(all_path[i], all_cost[i], all_path[i+1], all_cost[i+1],
                                                   now_crowd_density,target_crowd_density)
            for j in path:
                all_path_now.append(j)
            for k in cost:
                all_cost_now.append(k)
        else:
            target_crowd_density = dict_crowd_density_now[target_end]
            now_crowd_density = dict_crowd_density_now[now_end]
            path, cost = path_compare.path_compare(all_path[i], all_cost[i], all_path[i+1], all_cost[i+1],
                                                   now_crowd_density,target_crowd_density)
            for j in path:
                all_path_now.append(j)
            for k in cost:
                all_cost_now.append(k)
    return all_path_now, all_cost_now
"""this is for test"""
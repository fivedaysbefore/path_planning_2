# five days before
# 时间 2021/4/10 16:53
# five days before
# 时间 2021/4/10 15:54
def now_crowd_density(list_end_point_used, list_crowd_density):
    dict_crowd_density_now = {}
    crowd_density_temp = []
    used_point = []
    for i in range(len(list_end_point_used)):
        crowd_density_temp.append(tuple(list(map(int, (list_end_point_used[i], list_crowd_density[i])))))

    for i, k in enumerate(list_end_point_used):
        if k in used_point:
            continue
        else:
            used_point.append(k)
            density = crowd_density_temp[i][1]
            for j in range(i + 1, len(list_end_point_used)):
                if crowd_density_temp[i][0] == crowd_density_temp[j][0]:
                    density = density + crowd_density_temp[j][1]
        dict_crowd_density_now.update({k: density})
    return dict_crowd_density_now

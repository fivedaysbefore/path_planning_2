# five days before
# 时间 2021/4/18 17:55
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import time
import numpy as np
import math
from main import dict_net_node_coordinate
from main import list_net_edges
# 计算两点之间线段的距离
def __line_magnitude(x1, y1, x2, y2):
    lineMagnitude = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return lineMagnitude
#计算点到线段的距离
def __point_to_line_distance(point, line):
    px, py = point
    x1, y1, x2, y2 = line
    line_magnitude = __line_magnitude(x1, y1, x2, y2)
    if line_magnitude < 0.00000001:
        return 9999
    else:
        u1 = (((px - x1) * (x2 - x1)) + ((py - y1) * (y2 - y1)))
        u = u1 / (line_magnitude * line_magnitude)
        if (u < 0.00001) or (u > 1):
            # 点到直线的投影不在线段内, 计算点到两个端点距离的最小值即为"点到线段最小距离"
            ix = __line_magnitude(px, py, x1, y1)
            iy = __line_magnitude(px, py, x2, y2)
            if ix > iy:
                distance = iy
            else:
                distance = ix
        else:
            # 投影点在线段内部, 计算方式同点到直线距离, u 为投影点距离x1在x1x2上的比例, 以此计算出投影点的坐标
            ix = x1 + u * (x2 - x1)
            iy = y1 + u * (y2 - y1)
            distance = __line_magnitude(px, py, ix, iy)
        return distance

#def fire_diffusion(dict_net_node_coordinate,list_net_edges):
nodes = dict_net_node_coordinate
edges = list_net_edges

fire_x = 100
fire_y = 25
fire_speed = 0.1
fire_time = 0
while fire_time <= 200:
    print('time:',fire_time)
    list_disabled_point = []
    list_disabled_path = []
    fire_radius = fire_time*fire_speed
    """判断节点是否受到火势影响"""
    for i in range(1, len(nodes)+1):
        distance_node = np.sqrt((nodes[i][0]-fire_x)**2 + (nodes[i][1]-fire_y)**2)
        if distance_node > fire_radius:
            continue
        else:
            list_disabled_point.append(i)

    """判断路径是否受影响"""
    for j in range(len(edges)):
        start = edges[j][0]
        end = edges[j][1]
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        point = (fire_x, fire_y)
        line = (x1, y1, x2, y2)
        distance_edge = __point_to_line_distance(point, line)
        #print('distance_edge:', distance_edge)
        if start in list_disabled_point:
            continue
        elif end in list_disabled_point:
            continue
        else:
            point = (fire_x, fire_y)
            line = (x1, y1, x2, y2)
            distance_edge = __point_to_line_distance(point, line)
            # print('distance_edge:',distance_edge)
            if distance_edge < fire_radius:
                list_disabled_path.append(edges[j])
    print(list_disabled_point, list_disabled_path)
    time.sleep(5)
    fire_time += 5


# fig = plt.figure()
# ax = fig.add_subplot(111)
# cir1 = Circle(xy = (fire_x, fire_y), radius=fire_radius, alpha=0.5, color= 'red')
# ax.add_patch(cir1)
# ax.plot(fire_x, fire_y, 'ro')
#
# time.sleep(5)
# fire_time += 5

# return list_disabled_point, list_disabled_path

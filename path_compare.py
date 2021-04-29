# five days before
# 时间 2021/4/9 21:39
"""按原则进行路径比较，path_1为最优出口，path_2为次优出口"""
import xlwt
def path_compare(path_1,cost_1,path_2,cost_2,now_crowd_density,target_crowd_density):
    path = []
    cost = []
    max_crowd_density = 50
    if cost_1 <= 1.2*cost_2:
        path.append(path_1)
        cost.append(cost_1)
    elif target_crowd_density >= max_crowd_density:
        path.append(path_1)
        cost.append(cost_1)
    elif target_crowd_density+ now_crowd_density<=max_crowd_density:
        path.append(path_2)
        cost.append(cost_2)
    else:
        path.append(path_1)
        cost.append(cost_1)
        path.append(path_2)
        cost.append(cost_2)
    for j, path_i in enumerate(path):
        print("\n===The planning path :===")
        length = len(path_i) - 1
        print('path:', path_i[0], end='')
        for i in range(length):
            print(" -->", path_i[i+1], end='')
        #print('\npath:',path_i)
        print('\ncost:', cost[j])
        print('time:', int(cost[j]/1.7))
    return path, cost


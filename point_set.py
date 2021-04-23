# five days before
# 时间 2021/3/30 20:23
import xlrd

"""此函数用来读取路径的起点和终点，不可用点和不可用路径"""
def point_set(point_set_info):
    """考虑到紧急疏散时，疏散人群的分布是不确定的，同时出口还会受到紧急情况影响 """
    """因此我们以文件形式传递起点、终点信息，模拟船舱监控、传感器的实时跟新"""
    book_point = xlrd.open_workbook(point_set_info)
    start_end_info = book_point.sheets()[0]
    nrows_se = start_end_info.nrows
    ncols_se = start_end_info.ncols
    list_start_point = []
    list_end_point = []
    list_disabled_point = []
    list_disabled_path = []
    list_crowd_density = []
    start_end = []
    for row in range(1, nrows_se):
        start_end.append(start_end_info.row_values(row))
    for row in range(1, nrows_se):
        for col in range(ncols_se):
            if start_end[row - 1][col]:
                if col == 0:
                    list_start_point.append(int(start_end[row - 1][col]))
                elif col == 1:
                    list_end_point.append(int(start_end[row - 1][col]))
                elif col == 2:
                    list_disabled_point.append(int(start_end[row - 1][col]))
                elif col == 3:
                    list_disabled_path.append(tuple(list(map(int, start_end[row - 1][col:col + 2]))))
                elif col == 5:
                    list_crowd_density.append(int(start_end[row - 1][col]))
    return list_start_point, list_end_point, list_disabled_point, list_disabled_path, list_crowd_density

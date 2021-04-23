# five days before
# 时间 2021/3/30 17:10
import xlrd


def map_information(path_info):
    """该函数用来读取路径信息，包括路径起点、终点、长度、宽度、路径级别等"""
    book_2 = xlrd.open_workbook(path_info)
    path_information = book_2.sheets()[0]
    nrows_2 = path_information.nrows
    """获取路径信息文件的列数"""
    ncols_2 = path_information.ncols
    dict_path_info = {}
    """字典嵌套方式存储路径信息 大字典{路径标号：路径信息} 小字典：路径信息 {信息名称：具体信息}"""
    path_info_data = []
    """定义列表path_info_data一存储路径信息"""
    for row in range(1, nrows_2):
        path_info_data.append(path_information.row_values(row))
    """若要补充路径信息，只需在文件内添加并在第二个for循环内增加elif 结构即可"""
    for row in range(1, nrows_2):
        for col in range(0, ncols_2):
            if col == 0:
                start_num = int(path_info_data[row - 1][col])
            elif col == 1:
                end_num = int(path_info_data[row - 1][col])
            elif col == 2:
                path_length = path_info_data[row - 1][col]
            elif col == 3:
                path_width = path_info_data[row - 1][col]
            elif col == 4:
                path_level = int(path_info_data[row - 1][col])
            """用字典存储上述信息"""
        dict_path_info_tem = {
            'start_point': start_num,
            'end_point': end_num,
            'length': path_length,
            'width': path_width,
            'level': path_level
        }
        dict_path_info_tem_2 = {
            str(start_num) + ',' + str(end_num): dict_path_info_tem
        }
        dict_path_info.update(dict_path_info_tem_2)
    return dict_path_info

# five days before
# 时间 2021/4/29 19:09
def switch(node_pair):
    if node_pair[0] > node_pair[1]:
        node_pair = (node_pair[1],node_pair[0])
    return node_pair
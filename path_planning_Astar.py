# five days before
# 时间 2021/4/1 20:25
# -*- coding: utf-8 -*-
import time
def astar_path_finding(graph, nodes_NUM, start_point, end_point, h):
    # 问题的最终解
    class Stack:

        def __init__(self):
            self.stack = []

        def push(self, value):
            self.stack.append(value)
            return

        def pop(self):
            return self.stack.pop()

        def is_empty(self):
            if self.stack:
                return False
            return True

    # CLOSED表
    class Queue:
        def __init__(self):
            self.queue = []

        def put(self, value):
            self.queue.append(value)
            return

        def get(self):
            return self.queue.pop(0)

        def contain(self, value):
            return value in self.queue

        def is_empty(self):
            if self.queue:
                return False
            return True

    # OPEN表
    class PriorityQueue:

        def __init__(self):
            self.queue = []

        def put(self, node_cost):
            """
            :param node_cost: [value,cost]
            """
            self.queue.append(node_cost)


        def get(self):
            if self.queue:
                # """测试"""
                # print('self.queue:', self.queue)
                min_i = 0
                min_cost = self.queue[min_i][1]
                for i in range(len(self.queue)):
                    if self.queue[i][1] < min_cost:
                        min_i = i
                        min_cost = self.queue[i][1]
                return self.queue.pop(min_i)

        def contain(self, value):
            for i in range(len(self.queue)):
                if self.queue[i][0] == value:
                    return self.queue[i], True
            return None, False

        def is_empty(self):
            if self.queue:
                return False
            return True

    def a_star(graph, h, _root, _goal):
        g = [0] * nodes_NUM  # g(n) value                          现阶段搜索过程中的每个结点的g(n)记录@
        parents = [0] * nodes_NUM  # temporary parents             现阶段搜索过程中的每个节点的父结点记录@
        pq_open = PriorityQueue()  # open queue                     初始化open表@
        q_close = Queue()  # closed queue                           初始化closed表@
        s_path = Stack()  # solution nodes path                     s_path中作为走过路径记录@
        s_parent = Stack()  # solution nodes' parents path          s_parent中作为open表每次pop的记录@
        pq_open.put([_root, 0])  # 将初始结点存入OPEN表中@
        while pq_open.is_empty() == False:
            parent_node = pq_open.get()
            # """测试"""
            # print('goal:', _goal, 'parent_node:',parent_node)
            if parent_node[0] == _goal:
                break
            q_close.put(parent_node[0])
            for i in range(nodes_NUM):
                length = graph.get_edge(parent_node[0], i)
                if length != 0:
                    node, result = pq_open.contain(i)
                    f = parent_node[1] - h[parent_node[0]] + length + h[i]
                    # """测试"""
                    # print(parent_node[1], h[parent_node[0]], length, h[i])
                    # print('f:', f)
                    # """测试"""
                    if q_close.contain(i):
                        continue
                    elif result == True:
                        if node[1] > f:
                            #node.pop
                            parents[i] = parent_node[0]
                            pq_open.put([i, f])
                    else:
                        parents[i] = parent_node[0]
                        pq_open.put([i, f])
                        # """测试"""
                        # print('[i,f]:', [i, f])
        path = []
        cost = 0
        #print("parents:", parents)
        p = _goal
        time1 = time.time()
        while p != _root:
            time2 = time.time()
            run_time = time2 - time1
            if run_time > 0.001:
                cost = -1
                path = []
                break
            else:
                cost += graph.get_edge(p, parents[p])
                path.append(p);
                p = parents[p]
        path.append(start_point)
        list.reverse(path)
        return cost, path
    # place_str = input()
    # places = place_str.split()
    # cost = a_star(graph, h, eval(places[0]), eval(places[1]))
    cost, path = a_star(graph, h, start_point, end_point)
    #print('\n===A* algorithm The planning path===')
    return cost, path

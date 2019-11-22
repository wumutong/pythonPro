# 创建优化kNN算法的Kd树
# points为实例点集合,depth深度，为用来确定取维度的参数
from lib2to3.pytree import Node
from operator import itemgetter


def kd_tree(points,depth):
    if 0==len(points):
        return None
    # 指定 切分维度，len(points[0]) 是数据的实际维度，这样计算可以保证循环
    cutting_dim = depth % len(points[0])
    # 切分点初始化
    medium_index = len(points)
    # 对所有实例点按照指定维度进行排序，itemgetter用于获取对象哪些维度上的数据，参数
    # 为需要获取的数据在对象中的序号
    points.sort(key = itemgetter(cutting_dim))

    # 将该维度的中值点作为根节点
    node = Node(points[medium_index])
    # 对于左子树，重复构建（depth+1）
    node.left = kd_tree(points[:medium_index], depth + 1)
    # 对于右子树，重复构建（depth+1）
    node.right = kd_tree(points[medium_index + 1:], depth + 1)
    return node
"""
树有三种常用的存储方式：双亲表示法、孩子表示法、孩子兄弟表示法。

"""

"""
1. 双亲表示法
双亲表示法：在存储树的结点时，包括结点值data和该结点的双亲parent，
使用一组连续的存储单元存储树的每一个结点及结点间的关系。
存储结点的双亲时并不存储其值，存储的是其下标，对于根结点，因为没有双亲，所以设置parent=-1。

分析：
该存储结构在找某个结点的双亲时很容易，因为某个结点的双亲是唯一的，
但是找某个结点的孩子结点时，最坏情况下需要访问整个数组。
"""


# 定义树的一个结点：
class TreeNode1(object):
    def __init__(self, value=None):
        self.data = value
        self.parent = "-1"


"""
2. 孩子表示法
该方法的实现分为两部分，一部分是用data域来存储树的每一个结点值，
用FirstChild域来存储该结点第一个孩子结点的地址；另一部分是用指针链串起来的其他孩子结点。
分析：
查找孩子结点比较方便，但是找某个结点的双亲时最坏的情况就需要访问所有的数组元素及链表结点。
"""


# 定义树的根结点
class TreeNode2(object):
    def __init__(self):
        self.data = "#"
        self.fFirstChild = None


# 定义一个孩子结点
class ChildNode(object):
    def __init__(self):
        self.index = -1
        self.NextSibling = None


"""
3.孩子兄弟表示法
该方法又被称为二叉树表示法，每个结点包含3个部分，
即结点值data，指向该节点第一个孩子结点FirstChild，指向该结点的兄弟结点的NextSibling。

分析：
可以方便查找孩子结点和兄弟结点，但是查找结点双亲比较困难，可以考虑增加一个parent域，用于记录双亲结点。
"""


# 定义树的一个结点：
class TreeNode(object):
    def __init__(self, value=None):
        self.data = value
        self.FirstChild = None
        self.NextSibling = None

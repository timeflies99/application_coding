# -*-coding:UTF-8-*-


# todo 先声明一个二叉树结点
class BiNode(object):
    """class BiNode provide interface to set up a BiTree Node and to interact"""

    def __init__(self, element=None, left=None, right=None):
        """set up a node """
        self.element = element
        self.left = left
        self.right = right

    def get_element(self):
        """return node.element"""
        return self.element

    def dict_form(self):
        """return node as dict form"""
        dict_set = {
            "element": self.element,
            "left": self.left,
            "right": self.right,
        }
        return dict_set

    def __str__(self):
        """when print a node , print it's element"""
        return str(self.element)


# todo 实现二叉树.首先对二叉树进行初始化
class BiTree(object):
    """class BiTree provide interface to set up a BiTree and to interact"""

    def __init__(self, tree_node=None):
        """set up BiTree from BiNode and empty BiTree when nothing is passed"""
        self.root = tree_node

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def add_node_in_order(self, element):
        """add a node to existent BiTree in order"""
        node = BiNode(element)

        # if self.root is None:
        if self.is_empty():
            self.root = node
        else:
            node_queue = list()  # todo 这里可以看成是一个队列，创建一个队列
            node_queue.append(self.root)  # todo （进入队列），队尾添加操作
            print(len(node_queue))
            while len(node_queue):
                q_node = node_queue.pop(0)  # todo 从队列“出列”的操作，先进先出，队头出列操作
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

    """
    用一个列表元素按顺序构造.
    新添加的结点按顺序做为结点2的左子结点（这里不考虑像二叉查找树等的插入要求）。
    基本插入方法如下： 
    判断根结点是否存在，如果不存在则插入根结点。
    否则从根结点开始，判断左子结点是否存在，如果不存在插入, 如果左子结点存在判断右结点，不存在插入。
    如果左右结点存在，再依次遍历左右子结点的子结点，直到插入成功。
    上述的方法类似于层次遍历，体现了广度搜索优先的思想。
    因此从代码实现上，很显然需要一个队列对子结点进行入队与出队。
    """

    def set_up_in_order(self, elements_list):
        """set up BiTree from lists of elements in order """
        for elements in elements_list:
            self.add_node_in_order(elements)

    """
    通过字典进行初始树，可以借用层次遍历的思想实现树的构造，本质上其实就是对树进行一个非递归实现的拷贝
    """

    def set_up_from_dict(self, dict_instance):
        """set up BiTree from a dict_form tree using level traverse, or call it copy """
        if not isinstance(dict_instance, dict):
            return None
        else:
            dict_queue = list()  # todo 这里可以看成是一个队列，先进先出
            node_queue = list()  # todo 这里可以看成是一个队列，先进先出
            node = BiNode(dict_instance["element"])
            self.root = node  # 根节点，首先进队列
            node_queue.append(node)  # todo 这里可以看成队列的进列（进入队列），队尾添加操作
            dict_queue.append(dict_instance)  # todo 这里可以看成队列的进列（进入队列），队尾添加操作
            while len(dict_queue):  # todo 判断队列是否为空队列
                dict_in = dict_queue.pop(0)  # todo 从队列出列的操作，先进先出，队头出列操作
                node = node_queue.pop(0)  # todo 从队列出列的操作，先进先出，队头出列操作
                # in dict form, the leaf node might be irregular, like compressed to element type
                # Thus , all this case should be solved out respectively
                if isinstance(dict_in.get("left", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("left", None), dict):
                        dict_queue.append(dict_in.get("left", None))  # todo 根节点的孩子节点进队列
                        left_node = BiNode(dict_in.get("left", None)["element"])
                        node_queue.append(left_node)  # todo 入队列
                    else:
                        left_node = BiNode(dict_in.get("left", None))
                    node.left = left_node

                if isinstance(dict_in.get("right", None), (dict, int, float, str)):
                    if isinstance(dict_in.get("right", None), dict):
                        dict_queue.append(dict_in.get("right", None))
                        right_node = BiNode(dict_in.get("right", None)["element"])
                        node_queue.append(right_node)
                    else:
                        right_node = BiNode(dict_in.get("right", None))
                    node.right = right_node

    """
    往往我们也需要将一颗二叉树用字典的形式表示出来， 其方法与从字典初始化一棵二叉树一样
    """

    def pack_to_dict(self):
        """pack up BiTree to dict form using level traversal"""
        if self.root is None:
            return None
        else:
            node_queue = list()
            dict_queue = list()
            node_queue.append(self.root)
            dict_pack = self.root.dict_form()
            dict_queue.append(dict_pack)
            while len(node_queue):
                q_node = node_queue.pop(0)
                dict_get = dict_queue.pop(0)
                if q_node.left is not None:
                    node_queue.append(q_node.left)
                    dict_get["left"] = q_node.left.dict_form()
                    dict_queue.append(dict_get["left"])
                if q_node.right is not None:
                    node_queue.append(q_node.right)
                    dict_get["right"] = q_node.right.dict_form()
                    dict_queue.append(dict_get["right"])
        return dict_pack

    """
    求二叉树的深度或者高度的非递归实现，本质上可以通过层次遍历实现
    """

    def get_depth(self):
        """method of getting depth of BiTree"""
        if self.root is None:
            return 0
        else:
            node_queue = list()  # todo 创建队列
            node_queue.append(self.root)  # todo 进队列
            depth = 0
            while len(node_queue):
                q_len = len(node_queue)
                while q_len:
                    q_node = node_queue.pop(0)  # todo 出队列
                    q_len = q_len - 1
                    if q_node.left is not None:
                        node_queue.append(q_node.left)
                    if q_node.right is not None:
                        node_queue.append(q_node.right)
                depth = depth + 1
            return depth

    """
    前序遍历
二叉树的前序，中序，后序称体现的是“深度优先搜索”的思想。本质上它们的方法其实是一样的。 
    """

    def pre_traversal(self):
        """method of traversing BiTree in pre-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()  # todo 创建栈
            output_list = list()  # todo 创建栈
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' right,
                # pop the stack and get it's right node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop().right  # todo 出栈
                    continue
                #  save the front node and go next when left node exists
                while node.left is not None:
                    node_stack.append(node)  # todo 进栈
                    output_list.append(node.get_element())
                    node = node.left
                output_list.append(node.get_element())
                node = node.right
        return output_list

    """
    中序遍历的思想基本与前序遍历一样，只是最开始结点入栈时先不打印。
    只打印不存在左子树的当前结点，然后再出栈遍历右子树前再打印出来
    """

    def in_traversal(self):
        """method of traversing BiTree in in-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()  # todo 创建栈
            output_list = list()  # todo 创建栈
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' right,
                # pop the stack and get it's right node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop()  # todo 出栈，先进后出
                    # in in-order traversal, when pop up a node from stack , save it
                    output_list.append(node.get_element())  # todo 进栈，先进后出
                    node = node.right
                    continue
                # go-next when left node exists
                while node.left is not None:
                    node_stack.append(node)  # todo 进栈
                    node = node.left
                # save the the last left node
                output_list.append(node.get_element())
                node = node.right
        return output_list

    """
后序遍历的实现思想与前序、中序一样。有两种实现方式。 
先说第一种，同中序遍历，只是中序时从栈中pop出一个结点打印，并访问当前结点的右子树。 
后序必须在访问完右子树完，再打印该结点。
因此可先看栈顶点是否被访问过，如果访问过，即已经之前已经做了其右子树的访问因此可出栈，并打印，继续访问栈顶点。
如果未访问过，则对该点的访问标记置为访问，访问该点右子树。
可以发现，相对于前序与中序，后序的思想是一致的，只是需要多一个存储空间来表示结点状态。
    """

    def post_traversal1(self):
        """method of traversing BiTree in in-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' right,
                # pop the stack and get it's right node.
                # continue the circulating like this
                if node is None:
                    visited = node_stack[-1]["visited"]
                    # in in-order traversal, when pop up a node from stack , save it
                    if visited:
                        output_list.append(node_stack[-1]["node"].get_element())
                        node_stack.pop(-1)
                    else:
                        node_stack[-1]["visited"] = True
                        node = node_stack[-1]["node"]
                        node = node.right
                    continue
                # go-next when left node exists
                while node.left is not None:
                    node_stack.append({"node": node, "visited": False})
                    node = node.left
                # save the the last left node
                output_list.append(node.get_element())
                node = node.right
        return output_list

    """
    后续遍历还有一种访问方式。
    考虑到后续遍历是先左子树，
    再右子树再到父结点， 
    倒过来看就是先父结点， 
    再右子树再左子树。 
    是不是很熟悉， 是的这种遍历方式就是前序遍历的镜像试，除了改变左右子树访问顺序连方式都没变。 
    再将输出的结果倒序输出一遍就是后序遍历。 同样该方法也需要额外的空间存取输出结果。
    """

    def post_traversal2(self):
        """method of traversing BiTree in post-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' left,
                # pop the stack and get it's left node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop().left
                    continue
                while node.right is not None:
                    node_stack.append(node)
                    output_list.append(node.get_element())
                    node = node.right
                output_list.append(node.get_element())
                node = node.left
        return output_list[::-1]

    """
    # 求叶子节点
    求叶子节点有两种方法，一种是广度搜索优先，即如果当前节点存在左右子树将左右子树入队。
    如果当前节点不存在子树，则该节点为叶节点。继续出队访问下一个节点。直至队列为空，这个方法留给读者去实现。
    另外一种方法是，用深度搜索优先。 采用前序遍历，当判断到一个结点不存在左右子树时叶子结点数加一。
    """

    def get_leaf_num(self):
        """method of getting leaf numbers of BiTree"""
        if self.root is None:
            return 0
        else:
            node_stack = list()
            node = self.root
            leaf_numbers = 0
            # only node exists and stack is not empty that will do this circulation
            while node is not None or len(node_stack):
                if node is None:
                    """node is None then pop the stack and get the node.right"""
                    node = node_stack.pop().right
                    continue
                while node.left is not None:
                    node_stack.append(node)
                    node = node.left
                # if there is not  node.right, leaf_number add 1
                node = node.right
                if node is None:
                    leaf_numbers += 1
            return leaf_numbers

    """
    层次遍历（宽度优先遍历）
    """

    def BFS(self, root):
        pass

    """
    深度优先遍历
    """

    def DFS(self, root):
        pass


if __name__ == '__main__':
    dict_tree = {
        "element": 0,
        "left": {
            "element": 1,
            "left": {
                "element": 3,
                "left": 6,
                "right": 7,
            }
        },
        "right": {
            "element": 2,
            "left": 4,
            "right": {
                "element": 5,
                "left": 8,
                "right": 9,
            },
        },
    }

    a = BiTree()
    a.set_up_from_dict(dict_tree)
    # print(a.get_depth())
    print(a.pack_to_dict())

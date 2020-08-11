# -*-coding:UTF-8-*-


# 创建树的节点
class BiNode(object):
    def __init__(self, element=None, left=None, right=None):
        self.left = left
        self.element = element
        self.right = right

    def get_element(self):
        """
        返回树节点的值
        :return: node.element
        """
        return self.element

    def dict_form(self):
        """
        将节点打包成字典的格式返回
        :return: node as dict form
        """
        dict_node = {
            "element": self.element,
            "left": self.left,
            "right": self.right
        }
        return dict_node

    def __str__(self):
        return str(self.element)


# 创建一个二叉树
class BiTree(object):
    # 初始化二叉树
    def __init__(self):
        self.root = None  # todo 类似于链表中的头指针

    def is_empty(self):
        if self.root is None:
            return True
        return False

    # 用一个列表元素，按顺序取值插入二叉树中，该方法构造的为完全二叉树
    def set_up_with_list(self, elements_list):
        for element in elements_list:
            self.add_node(element)

    def add_node(self, element):
        node = BiNode(element)

        if self.is_empty():
            self.root = node

        else:
            # todo 创建一个队列来存储节点,入列，队列先进先出
            node_queue = list()

            # 添加根节点
            node_queue.append(self.root)
            print(len(node_queue))

            while len(node_queue):
                # todo 从队列中弹出数据，出列,队列先进先出
                queue_node = node_queue.pop(0)

                if queue_node.left is None:
                    queue_node.left = node
                    break
                elif queue_node.right is None:
                    queue_node.right = node
                    break
                else:
                    node_queue.append(queue_node.left)
                    node_queue.append(queue_node.right)

    # 用一个字典元素来插入值，实际少用
    def set_up_with_dict(self, elements_dict):
        if not isinstance(elements_dict, dict):
            return None

        # todo 同样还是创建队列来存储节点,此处创建两个队列存储
        dict_in_queue = list()
        node_in_queue = list()

        node = BiNode(elements_dict["element"])  # 此处的node为根节点
        self.root = node

        node_in_queue.append(node)  # todo 这里进入队列的是节点
        dict_in_queue.append(elements_dict)  # todo 这里进入队列的是字典
        # todo 递归的思想
        while len(dict_in_queue):

            # todo 采用双指针的方式
            queue_node = node_in_queue.pop(0)  # 首次取出的是根节点

            dict_data = dict_in_queue.pop(0)  # 首次取出的是整个字典
            left = dict_data.get("left", None)
            right = dict_data.get("right", None)

            if isinstance(left, (dict, int, float, str)):
                if isinstance(left, dict):
                    dict_in_queue.append(left)
                    left_node = BiNode(left["element"])
                    node_in_queue.append(left_node)  # 将该节点保存，下次循环就当做上一个的节点，直接接在前面即可
                else:
                    left_node = BiNode(left)

                queue_node.left = left_node

            if isinstance(right, (dict, int, float, str)):
                if isinstance(right, dict):
                    dict_in_queue.append(right)
                    right_node = BiNode(right["element"])
                    node_in_queue.append(right_node)
                else:
                    right_node = BiNode(right)

                queue_node.right = right_node

    # 往往我们也需要将一颗二叉树用字典的形式表示出来，其方法与从字典初始化一棵二叉树一样
    def tree_to_dict(self):
        if self.root is None:
            return None
        node_in_queue = list()
        dict_in_queue = list()

        node_in_queue.append(self.root)
        dict_pack = self.root.dict_form()
        dict_in_queue.append(dict_pack)

        while len(node_in_queue):
            q_node = node_in_queue.pop(0)
            dict_get = dict_in_queue.pop(0)

            if q_node.left:
                node_in_queue.append(q_node.left)  # todo 加入队列中进行下一次的遍历
                dict_get["left"] = q_node.left.dict_form()
                dict_in_queue.append(dict_get["left"])  # todo 加入队列中进行下一次的头节点

            if q_node.right:
                node_in_queue.append(q_node.right)
                dict_get["right"] = q_node.right.dict_form()
                dict_in_queue.append(dict_get["right"])
        return dict_pack

    """
    求二叉树的深度或者高度的非递归实现，本质上可以通过层次遍历实现
    """

    def get_tree_depth(self):
        if self.is_empty():
            return 0

        # # 创建队列
        count = 0
        tree_queue = list()
        tree_queue.append(self.root)

        while len(tree_queue):
            q_len = len(tree_queue)
            while q_len:
                node = tree_queue.pop(0)
                q_len -= 1
                if node.left:
                    tree_queue.append(node.left)
                if node.right:
                    tree_queue.append(node.right)
            count += 1

    # DFS
    """
    前序遍历:根-左-右
    二叉树的前序，中序，后序称体现的是“深度优先搜索”的思想。本质上它们的方法其实是一样的。 
    """

    def __pre_traversal_1(self, curs, out_tree, tree_stack):
        while curs:
            out_tree.append(curs.element)
            if curs.right:
                tree_stack.append(curs.right)
            curs = curs.left

        return tree_stack

    def pre_traversal(self):
        if self.is_empty():
            return None

        out_tree = []
        # todo 创建栈，用来存储右节点
        tree_stack = list()

        cur = self.root  # 头指针
        tree_stack = self.__pre_traversal_1(cur, out_tree, tree_stack)
        while len(tree_stack):
            cur2 = tree_stack.pop()
            self.__pre_traversal_1(cur2, out_tree, tree_stack)
        return out_tree

    """
    中序遍历：左-根-右
    中序遍历的思想基本与前序遍历一样，只是最开始结点入栈时先不打印。
    只打印不存在左子树的当前结点，然后再出栈遍历右子树前再打印出来
    """

    def __in_traversal_1(self, cur, out_tree, tree_stack):
        while isinstance(cur, (int, BiNode)):
            if isinstance(cur, int):
                out_tree.append(cur)
                break

            if cur.left:
                tree_stack.append(cur.right)
                tree_stack.append(cur.element)
            else:
                out_tree.append(cur.element)
                if cur.right:
                    tree_stack.append(cur.right)
            cur = cur.left

    def in_traversal(self):
        if self.is_empty():
            return None

        out_tree = []
        # todo 创建栈，用来存储根-右节点
        tree_stack = list()
        cur = self.root  # todo 头指针
        self.__in_traversal_1(cur, out_tree, tree_stack)
        while len(tree_stack):
            cur2 = tree_stack.pop()
            self.__in_traversal_1(cur2, out_tree, tree_stack)

        return out_tree

    def __post_traversal_1(self, cur, out_tree, tree_stack):
        while isinstance(cur, (int, BiNode)):
            if isinstance(cur, int):
                out_tree.append(cur)
                break

            if cur.left:
                tree_stack.append(cur.element)
                tree_stack.append(cur.right)
            else:
                out_tree.append(cur.element)
                if cur.right:
                    tree_stack.append(cur.right)
            cur = cur.left

    def post_traversal(self):
        if self.is_empty():
            return None

        out_tree = []
        # todo 创建栈，用来存储根-右节点
        tree_stack = list()
        cur = self.root  # todo 头指针
        self.__post_traversal_1(cur, out_tree, tree_stack)
        while len(tree_stack):
            cur2 = tree_stack.pop()
            self.__post_traversal_1(cur2, out_tree, tree_stack)

        return out_tree

    def bfs(self):


        # todo 创建一个队列
        tree_queue = list()


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
    tree = BiTree()
    tree.set_up_with_dict(dict_tree)
    # print(tree.tree_to_dict())
    # print(tree.pre_traversal())
    print(tree.in_traversal())
    print(tree.post_traversal())

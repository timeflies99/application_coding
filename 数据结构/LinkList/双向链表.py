# -*-coding:UTF-8-*-

"""
常用操作：
is_empty() :判断链表是否为空，空则返回True，否则返回False。
length(): 返回链表的长度。
travel():遍历链表并打印其中的元素。
add(item):往链表头部添加元素。
append(item):往链表尾部添加元素。
insert(pos, item):往指定位置添加元素。
search(item):查找某个元素是否存在，存在则返回True，否则返回False。
find(item):查找某个元素是否存在，存在则返回其索引，否则返回-1。
remove(item):删除指定的某个元素。
pop(pos):删除指定位置的元素，删除成功则返回该位置元素，否则返回None。
"""


# 创建双向节点
class Node(object):
    def __init__(self, value=None):
        self.before = None
        self.value = value
        self.next = None


class BiLinkList(object):
    def __init__(self):
        # head = Node()
        # tail = Node()
        # self.head = head
        # self.tail = tail
        # self.head.next = self.tail
        # self.tail.before = self.head
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def __len__(self):
        if self.is_empty():
            return 0
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def add(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.before = node
            self.head = node

    def append(self, val):
        if self.is_empty():
            self.add(val)
        else:
            node = Node(val)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.before = cur

    def insert(self, pos, val):
        node = Node(val)
        assert isinstance(pos, int)

        if self.is_empty():
            node.next = self.head
            self.head.before = node
            self.head = node
        else:
            cur = self.head
            pre = None
            if pos <= 0:
                node.next = self.head
                self.head.before = node
                self.head = node
            elif pos >= self.__len__():
                cur = self.head
                pre = None
                while cur:
                    pre = cur
                    cur = cur.next
                pre.next = node
                node.before = pre
            else:
                for i in range(pos + 1):
                    if i == pos - 1:
                        pre = cur
                        cur = cur.next
                        break
                    cur = cur.next
                pre.next = node
                node.next = cur
                node.before = pre
                cur.before = node

    def search(self, val):
        if self.is_empty():
            return False
        else:
            cur = self.head
            while cur:
                if val == cur.value:
                    return True
                cur = cur.next
            return False

    def find(self, val):
        if self.is_empty() or not self.search(val):
            return -1
        else:
            count = 0
            cur = self.head
            while cur:
                if val == cur.value:
                    return count
                count += 1
                cur = cur.next
            return -1

    def remove(self, val):
        if self.is_empty():
            print("this is empty")
        elif not self.search(val):
            print("this is not in link_list")
        else:
            count = 0
            pre = None
            cur = self.head
            while cur:
                if cur.value == val:
                    if count == 0:
                        self.head = cur.next
                        cur.next.before = self.head
                    else:
                        pre.next = cur.next
                        cur.next.before = pre
                    break
                else:
                    pre = cur
                    cur = cur.next
                count += 1
            else:
                print("this is not in link_list")

    def pop(self, pos):
        assert isinstance(pos, int)
        if self.is_empty():
            raise IndexError
        else:
            cur = self.head
            pre = None

            if pos <= 0:
                val = cur.value
                self.head = cur.next
                return val
            elif pos >= self.__len__():
                while cur.next:
                    pre = cur
                    cur = cur.next
                pre.next = None
                val = cur.value
                return val
            else:
                for i in range(pos + 1):
                    if i == pos - 1:
                        pre = cur
                        cur = cur.next
                        break
                    cur = cur.next
                pre.next = cur.next
                cur.next.before = pre
                val = cur.value
                return val

    def travel(self):
        if self.is_empty():
            print("this is empty")
        else:
            cur = self.head
            while cur:
                val = cur.value
                print(val, sep=" ", end=" ")
                cur = cur.next
            print()


if __name__ == '__main__':
    bi_link = BiLinkList()
    bi_link.add(6)
    bi_link.add(8)
    bi_link.append(9)
    bi_link.append(7)
    bi_link.insert(1, 5)
    # print(bi_link.is_empty())
    # print(len(bi_link))
    # print(bi_link.search(0))
    # print(bi_link.find(8))
    bi_link.travel()
    # bi_link.remove(4)
    print(bi_link.pop(3))
    print("-" * 30)
    bi_link.travel()

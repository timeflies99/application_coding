# -*-coding:UTF-8-*-
# -*-coding:UTF-8-*-

"""
常用操作：
is_empty() :判断链表是否为空，空则返回True，否则返回False。
length(): 返回链表的长度。
travel():遍历链表并打印其中的元素。
add(item):往链表头部添加元素。
append(item):往链表尾部添加元素。
insert(pos, item):往指定位置添加元素。
pop(pos):删除指定位置的元素，删除成功则返回该位置元素，否则返回None。
remove(item):删除指定的某个元素。
search(item):查找某个元素是否存在，存在则返回True，否则返回False。
find(item):查找某个元素是否存在，存在则返回其索引，否则返回-1。
"""


# 创建链表的节点
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


# 创建单向链表
class LinkList(object):
    def __init__(self):
        self.head = None
        # self.tail = None

    def __str__(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            cur = self.head
            count = 0
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
            self.head = node

    def append(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, num, val):

        assert isinstance(num, int)
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            if num <= 0:
                node.next = self.head
                self.head = node
            elif num >= self.__len__():
                self.append(val)
            else:
                pre = None
                cur = self.head
                for count in range(num + 1):
                    if count == num - 1:
                        pre = cur
                        cur = cur.next
                        break
                    cur = cur.next

                node.next = cur
                pre.next = node

    def find(self, val):
        if self.is_empty():
            return -1
        elif not self.search(val):
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

    def search(self, val):
        if self.is_empty():
            return False
        cur = self.head
        while cur:
            if val == cur.value:
                return True
            cur = cur.next
        return False

    def pop(self, pos):
        assert isinstance(pos, int)
        if self.is_empty():
            raise IndexError
        else:
            cur = self.head
            if pos <= 0:
                val = cur.value
                self.head = cur.next
                return val
            elif pos >= self.__len__():
                cur = self.head
                pre = None
                while cur.next:
                    pre = cur
                    cur = cur.next
                if pre is None:
                    pre = self.head
                pre.next = None
                val = cur.value
                return val
            else:
                pre = None
                cur = self.head
                for count in range(pos + 1):
                    if count == pos - 1:
                        pre = cur
                        cur = cur.next
                        break
                    cur = cur.next
                val = cur.value
                pre.next = cur.next
                return val

    def remove(self, val):
        if not self.search(val):
            print("value is not in link_list")
        else:
            cur = self.head
            pre_node = None
            count = 0
            while cur:
                if cur.value == val:
                    if count == 0:
                        self.head = cur.next
                    else:
                        pre_node.next = cur.next
                    break
                else:
                    pre_node = cur
                    cur = cur.next
                count += 1

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


class Solution:
    def __init__(self):
        self.ll = []

    def reversePrint(self, head):

        if head:
            value = head.value
            self.ll.append(value)
            if head.next:
                self.reversePrint(head.next)
            return self.ll[::-1]
        else:
            return self.ll


if __name__ == '__main__':
    link = LinkList()
    link.add(3)
    link.add(4)
    link.append(6)
    link.travel()

    link = link.head
    res = Solution().reversePrint(link)
    print(res)

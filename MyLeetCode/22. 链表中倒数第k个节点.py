# -*-coding:UTF-8-*-
"""

输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个节点是值为4的节点。

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

    def daoshu(self, k):
        if self.is_empty():
            return None
        fast, slow = self.head, self.head

        for i in range(k):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        if not slow:
            print("this is empty")
        else:
            cur = slow
            while cur:
                val = cur.value
                print(val, sep=" ", end=" ")
                cur = cur.next
            print()


if __name__ == '__main__':
    # todo 双指针法
    k = 4
    link = LinkList()
    link.append(3)
    link.append(4)
    link.append(5)
    link.append(6)
    link.travel()
    link.daoshu(k)

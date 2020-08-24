# -*-coding:UTF-8-*-
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

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
        self.ll = []

    # def __str__(self):
    #     return self.travel()

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

    # 遍历打印链表
    def travel(self, label=None):
        if not label:
            link_list = self.head
        else:
            link_list = label

        if not link_list:
            print("this is empty")
        else:
            cur = link_list
            while cur:
                val = cur.value
                print(val, sep=" ", end=" ")
                cur = cur.next
            print()

    # 获取倒数K个数的链表
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

    # 从尾到头打印链表
    def reversePrint(self, cur=None):
        if not cur:
            head = self.head
        else:
            head = cur
        if head:
            value = head.value
            self.ll.append(value)
            if head.next:
                self.reversePrint(head.next)
            return self.ll[::-1]
        else:
            return self.ll

    # 反转链表
    def reverseList(self):

        if self.is_empty():
            return []
        elif not self.head.next:
            return [self.head.value]

        else:
            new_link = None
            cur = self.head
            while cur:
                new_node = Node(cur.value)
                new_node.next = new_link
                new_link = new_node
                cur = cur.next
            self.travel(label=new_link)
            # return new_link


# 合并两个有序链表
def mergeTwoLists1(l1, l2):
    if l1 == None:
        return l2
    elif l2 == None:
        return l1

    if l1.value <= l2.value:
        l1.next = mergeTwoLists1(l1.next, l2)
        return l1
    elif l2.value < l1.value:
        l2.next = mergeTwoLists1(l1, l2.next)
        return l2


# 合并两个有序链表
def mergeTwoLists2(l1, l2):
    new_link = LinkList()

    if l1.value <= l2.value:
        new_link.append(l1.value)
        l1 = l1.next

# 合并两个无序链表
# def mergeTwoLists3(l1, l2)

if __name__ == '__main__':
    link1 = LinkList()
    link1.append(1)
    link1.append(2)
    link1.append(4)
    link2 = LinkList()
    link2.append(1)
    link2.append(3)
    link2.append(5)
    link2.append(7)

    # link1.travel()
    # link2.travel()
    res = mergeTwoLists1(link1.head, link2.head)
    print(res)

# -*-coding:UTF-8-*-
class ListNode(object):
    def __init__(self, value=None):
        self.val = value
        self.next = None


from collections import deque


# 迭代法
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:

        # 利用队列实现迭代算法
        if not head:
            return []
        elif head.next is None:
            return head

        collect = list()
        while head.next:
            collect.append(head)
            head = head.next

        # 此时head指向最后一个不为空的节点
        temp = head
        while collect:
            node = collect.pop()
            node.next = None
            temp.next = node
            temp = node
        return head


# 递归法
class Solution2:
    def move_single(self, head, temp):
        # 这里不能用val代替对象来进行条件判断，除非规定所有val都不同，所以比较两个节点的对象
        if head.next != temp:
            # 递归不会覆盖之前的数据，类似回复现场，因此要手动替换temp
            temp = self.move_single(head.next, temp)
        head.next = None
        temp.next = head
        temp = head
        return temp

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 递归算法
        if not head:
            return []
        if not head.next:
            return head

        temp = head
        while temp.next:
            temp = temp.next

        # 此时temp到达了最后一个不为空的节点
        result = temp
        self.move_single(head, temp)
        return result


# 双指针法
class Solution3:
    def reverseList(self, head):
        if head is None:
            return []
        elif head.next is None:
            return head

        cur = head
        end = None
        while cur:
            node = ListNode(cur.val)
            node.next = end
            end = node
            cur = cur.next

        return end

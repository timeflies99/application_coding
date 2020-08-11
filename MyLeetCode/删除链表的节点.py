# -*-coding:UTF-8-*-
"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def deleteNode(self, head, val):
        """

        :param head: listNode
        :param val: int
        :return: listNode
        """

        cur = head

        if node.get("val") == val:
            return node.get("next")

        while node:
            if node.get("next").get("val") == val:
                node["next"] = node.get("next").get("next")
                break
            node = node.get("next")
        return head


if __name__ == '__main__':
    # head = ListNode{val:4,next:ListNode{val:5,next:ListNode{val:1,next:ListNode{val:9,next:None}}}}
    head = {"val": 4, "next": {"val": 5, "next": {"val": 1, "next": {"val": 9, "next": None}}}}
    val = 9
    print(Solution().deleteNode(head, val))

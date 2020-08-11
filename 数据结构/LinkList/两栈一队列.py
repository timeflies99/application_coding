# -*-coding:UTF-8-*-


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            count = 0
            cur = self.head
            while cur:
                count += 1
                cur = cur.next
            return count

    def __append(self, node):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def push(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            self.__append(node)

    def pop(self):
        if self.is_empty():
            raise Error
        else:
            cur = self.head
            pre = None
            while cur.next:
                pre = cur
                cur = cur.next
            if pre is None:
                pre = self.head
                self.head = None
            pre.next = None
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


class Error(object):
    def __init__(self):
        self.item = "I'm sorry"

    def __str__(self):
        return self.item


# class Queue(object):
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         if self.head is None:
#             return True
#         return False
#
#     def __len__(self):
#         if self.is_empty():
#             return 0
#         else:
#             count = 0
#             cur = self.head
#             while cur:
#                 count += 1
#                 cur = cur.next
#             return count
#
#     def __append(self, node):
#         cur = self.head
#         while cur.next:
#             cur = cur.next
#         cur.next = node
#
#     def push(self, val):
#         node = Node(val)
#         if self.is_empty():
#             self.head = node
#         else:
#             self.__append(node)
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError
#         else:
#             cur = self.head
#             self.head = cur.next
#             val = cur.value
#             return val
#
#     def travel(self):
#         if self.is_empty():
#             print("this is empty")
#         else:
#             cur = self.head
#             while cur:
#                 val = cur.value
#                 print(val, sep=" ", end=" ")
#                 cur = cur.next
#             print()


# 两栈实现一队列
class Stack2Queue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def queue_is_empty(self):
        if self.stack2.is_empty() and self.stack1.is_empty():
            return True
        return False

    def push(self, val):
        self.stack1.push(val)

    def pop(self):
        if self.queue_is_empty():
            raise Error
        else:
            if self.stack2.is_empty():
                length = len(self.stack1)
                for i in range(length):
                    self.stack2.push(self.stack1.pop())
                return self.stack2.pop()
            else:
                return self.stack2.pop()


if __name__ == '__main__':
    # sq = Stack2Queue()
    # sq.push(9)
    # # sq.push(2)
    # # sq.push(3)
    # print(sq.pop())
    # print(sq.pop())
    # print(sq.pop())
    s = Stack()
    s.push(9)
    print(s.pop())
    print(s.pop())

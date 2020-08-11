# -*-coding:UTF-8-*-
"""
栈先进后出，只能在栈顶进行删除和操作（出列）

"""


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
        node.next = self.head
        self.head = node

    def push(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            self.__append(node)

    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            val = self.head.value
            self.head = self.head.next
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
    stack = Stack()
    stack.push(5)
    stack.push(10)
    # print(stack.is_empty())
    stack.travel()
    print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # stack.travel()

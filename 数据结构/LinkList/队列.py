# -*-coding:UTF-8-*-

"""
队列先进先出，只能在队头进行删除操作（出列），只能在队尾进行添加操作（入列）

"""


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue(object):
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
    queue = Queue()
    print(queue.is_empty())
    queue.push(5)
    queue.push(10)
    queue.travel()
    print(queue.pop())
    # print(queue.pop())
    # print(queue.pop())

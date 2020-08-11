# # -*-coding:UTF-8-*-
#
# # python 实现哈希表
#
#
# class HashTable:
#     """
#     哈希函数的构造
#     解决冲突
#     """
#
#     def __init__(self, source):
#         self.source = source
#         self._index = []
#         self._val = []
#         self.table = []
#         self._mod = 13
#
#     def Output(self):
#         print(self._index)
#         print(self._val)
#
#     def _create_table(self):
#         """
#         初始化哈希表
#         哈希表长度最短为取余因子_mod,一般为源数据长度
#         """
#         if len(self.source) < self._mod:
#             length = self._mod
#         else:
#             length = len(self.source)
#
#         self._index = [i for i in range(length)]
#         self._val = [None for i in range(length)]
#
#     def _func_hash(self):
#         """
#         构建哈希函数
#         """
#         for sour in self.source:
#             remainder = sour % self._mod
#             if self._val[remainder] is None:
#                 self._val[remainder] = sour
#             else:
#                 # 处理冲突
#                 rem = remainder
#                 while self._val[rem] is not None:
#                     if rem + 1 >= len(self._val):
#                         rem = -1
#                     rem += 1
#                 self._val[rem] = sour
#         self.table = list(zip(self._index, self._val))
#
#     def get(self, num):
#         """
#         查找
#         """
#         rem = num % self._mod
#         if self._val[rem] != num:
#             while True:
#                 if rem + 1 >= len(self._val):
#                     rem = 0
#                 if self._val[rem] == num:
#                     break
#                 rem += 1
#         return rem
#
#     def run(self):
#         self._create_table()
#         self._func_hash()
#         self.Output()
#
#
# if __name__ == '__main__':
#     test = [12, 15, 17, 21, 22, 25, 13, 0]
#     h = HashTable(test)
#     h.run()
#     print(h.get(17))

"""
线性表结构
"""


class LinearMap(object):

    def __init__(self):
        self.items = []

    # 往表中添加元素
    def add(self, k, v):
        self.items.append((k, v))

    # 线性方式查找元素
    def get(self, k):
        for key, value in self.items:
            if key == k:  # 键存在，返回值，否则抛出异常
                return value
        raise KeyError

    def print_l(self):
        print(self.items)


'''
我们可以在使用add添加元素时让items列表保持有序，而在使用get时采取二分查找方式，时间复杂度为O(log n)。 
然而往列表中插入一个新元素实际上是一个线性操作，所以这种方法并非最好的方法。
同时，我们仍然没有达到常数查找时间的要求。
'''

# line_map = LinearMap()
# line_map.add("a", 2)
# line_map.add("b", 3)
# line_map.add("a", 1)
# line_map.print_l()
# print(line_map.get("a"))
# ---------------------------------------------------------
'''
将总查询表分割为若干段较小的列表，比如100个子段。
通过hash函数求出某个键的哈希值，再通过计算，得到往哪个子段中添加或查找。
相对于从头开始搜索列表，时间会极大的缩短。
'''


class BetterMap(object):
    # 利用LinearMap对象作为子表，建立更快的查询表
    def __init__(self, n=100):
        self.maps = []  # 总表格
        for i in range(n):  # 根据n的大小建立n个空的子表
            self.maps.append(LinearMap())

    def find_map(self, k):  # 通过hash函数计算索引值
        index = hash(k) % len(self.maps)
        return self.maps[index]  # 返回索引子表的引用

    # 寻找合适的子表（linearMap对象）,进行添加和查找
    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)


line_map = BetterMap()
line_map.add("a", 2)
line_map.add("b", 3)
line_map.add("a", 1)
# line_map.print_l()
print(line_map.get("a"))

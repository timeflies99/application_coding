# -*-coding:UTF-8-*-
"""
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 
限制：

0 <= n <= 1000

0 <= m <= 1000

"""


def findNumberIn2DArray(matrix, target):
    return True if target in {s for val in matrix for s in val} else False


def findNumberIn2DArray2(matrix, target):
    rows = len(matrix)
    if rows == 0:
        return False

    cols = len(matrix[0])
    if cols == 0:
        return False

    # 从右上角开始查找
    x = 0
    y = cols - 1
    while x < rows and y >= 0:
        if target == matrix[x][y]:
            return True
        elif target < matrix[x][y]:
            y -= 1
        else:
            x += 1
    return False


if __name__ == '__main__':
    a = [[1, 4, 7, 11, 15],
         [2, 5, 8, 12, 19],
         [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24],
         [18, 21, 23, 26, 30]]
    # print(a)
    s = findNumberIn2DArray2(a, 10000)
    print(s)

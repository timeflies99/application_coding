# -*-coding:UTF-8-*-

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

"""


# todo

def uniquePaths(m: int, n: int) -> int:
    # 初始化为１，避免多余的赋值，外层不使用*，否则浅拷贝内层可能会在赋值时候出现问题
    dp = [[1] * n for _ in range(m)]
    print(dp)
    for i in range(1, m):
        for j in range(1, n):
            # dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            print(i, j)
            a = dp[i][j - 1]
            b = dp[i - 1][j]
            dp[i][j] = a + b

    return dp[-1][-1]


def uniquePathsWithObstacles(obstacleGrid) -> int:
    m = len(obstacleGrid)
    if m < 1:
        return 0
    n = len(obstacleGrid[0])
    if n < 1:
        return 0
    if 1 == obstacleGrid[0][0]:
        return 0
    dp = [[0] * n for _ in range(m)]  # 外层不能使用*，否则会浅拷贝内层，赋值会带来问题，初始化为０，可以避免额外的赋值
    print(dp)
    for i in range(0, m):
        for j in range(0, n):
            if 0 == i and 0 == j:
                dp[i][j] = 1
            elif 0 == i and 0 != j:
                if 0 == obstacleGrid[i][j]:
                    dp[i][j] = dp[i][j - 1]
            elif 0 != i and 0 == j:
                if 0 == obstacleGrid[i][j]:
                    dp[i][j] = dp[i - 1][j]
            else:
                if 0 == obstacleGrid[i][j]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    m, n = 4, 5
    # m, n = eval(input("please input two number ,like: [2,3]:"))
    # assert isinstance(m, int)
    # assert isinstance(n, int)
    # res = uniquePaths(m, n)
    # print(res)

    s = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    res = uniquePathsWithObstacles(s)
    print(res)

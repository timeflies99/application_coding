# -*-coding:UTF-8-*-
import numpy as np

a = np.arange(1, 13).reshape(4, 3)
m, n = a.shape

num1 = int(m / 2) if m % 2 else int((m + 1) / 2)
# num2 = int(n / 2) if n % 2 else int((n - 1) / 2)
# print(num1)
# print(num2)
res = []
for i in range(num1):
    res.append(a[i, i:])
    res.append(a[i + 1:, -1-i])
    res.append(a[-1-i, :-1])
    res.append(a[-1, :-1])

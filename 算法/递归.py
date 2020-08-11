# -*-coding:UTF-8-*-


def add(x):
    if x <= 1:
        return 1
    else:
        return add(x - 1)


print(add(5))

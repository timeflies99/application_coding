# -*-coding:UTF-8-*-


def hammingWeight(n):
    assert isinstance(n, int)
    n = bin(n)
    n = str(n).replace("0", "").replace("b", "")
    return len(n)


if __name__ == '__main__':
    n = input("please input your number:")

    print(hammingWeight(5))

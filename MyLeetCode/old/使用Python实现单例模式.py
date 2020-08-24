# -*-coding:UTF-8-*-


class Demo(object):
    def __new__(cls, *args):
        if not hasattr(cls, "c1"):
            cls.c1 = super().__new__(cls)
        return cls.c1

    def __init__(self, s):
        self.s1 = s

    def __repr__(self):
        return "this demo is {}   attr1 is {}".format(id(self), self.s1)


if __name__ == '__main__':
    a = Demo("aaa")
    print(a)
    b = Demo("bbb")
    print(b)

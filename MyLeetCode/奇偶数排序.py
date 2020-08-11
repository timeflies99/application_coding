# -*-coding:UTF-8-*-
def exchange(nums):
    qi = []
    ou = []
    [ou.append(nums[i]) if nums[i] % 2 == 0 else qi.append(nums[i]) for i in range(len(nums))]
    return qi + ou


if __name__ == '__main__':
    print(len([2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]))
    r = exchange([2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1])
    print(r)

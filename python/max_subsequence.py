"""
最长连续子序列
encoding=utf-8
_author = youzipi
date = 17/2/14
"""
empty_list = []


def find_max_sub(seq=empty_list):
    max_sum = 0
    max_start = 0
    max_end = 0

    max_suffix_sum = 0
    max_suffix_start = 0
    max_suffix_end = 0

    for index, item in enumerate(seq):
        next_max_suffix_sum = max_suffix_sum + item
        if next_max_suffix_sum < 0:
            max_suffix_sum = 0
            max_suffix_start = index + 1
            max_suffix_end = index + 1
        else:
            max_suffix_sum = next_max_suffix_sum
            max_suffix_end = index

        if next_max_suffix_sum > max_sum:
            max_sum = next_max_suffix_sum
            max_start = max_suffix_start
            max_end = max_suffix_end

    return seq[max_start:max_end + 1], max_sum


if __name__ == '__main__':
    a = [2, -3, 1.5, -1, 3, -2, -3, 3]
    max_sub, max_sum = find_max_sub(a)
    print("max_sub=", max_sub)
    print("max_sum=", max_sum)

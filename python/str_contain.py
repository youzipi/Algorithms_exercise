# coding=utf-8
"""
给定的s1,s2，判断s2是否在s1的循环移位的字符串中存在
"""

s1 = 'abcd'
s2 = 'da'
s3 = 'bbc'


def contain1(s, ss):
    length = len(s)
    for i in range(length):
        temp = s[i:] + s[:i]
        if ss in temp:
            print(temp)
            return True
    return False


def contain2(s, ss):
    length = len(s)
    temp = s + s
    if ss in temp:
        print(temp)
        return True
    return False


print(contain1(s1, s2))
print(contain1(s1, s3))
print(contain2(s1, s2))
print(contain2(s1, s3))

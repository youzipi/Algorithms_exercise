# -*- coding: utf-8 -*- 
# user: youzipi
# date: 15-10-14 下午3:09
import random


def quick_sort(a):
    return quick_sort2(a, 0, len(a) - 1)


def quick_sort2(a, low, high):
    length = high - low
    if length <= 1:
        return a

    ran = random.randint(low, high - 1)
    left = low + 1
    right = high
    flag = a[ran]
    a[low], a[ran] = a[ran], a[low]
    while True:
        while a[left] < flag:  # 向右寻找大于flag的数
            left += 1
            if left == high:
                break
        while a[right] > flag:  # 向左寻找小于flag的数
            right -= 1
            if right == low:
                break
        if left < right:
            a[left], a[right] = a[right], a[left]
            print a
        else:
            break
    print a
    a[low], a[right] = a[right], a[low]
    quick_sort2(a, low, right - 1)
    quick_sort2(a, right + 1, high)
    return a


a = [2, 8, 9, 4, 5, 6, 7, 1, 0, 3, ]
print quick_sort(a)

# -*- coding: utf-8 -*-


"""
describe:

插入排序

时间复杂度是n^2,此算法对于少量还可以，比较稳定
但是，对于大量的数据会造成内存问题，也会有时间上的缓慢问题
考虑到算法，不建议用这个排序算法

算法思想：
    将数组分为2部分，前部分是已经排好序的数组，后部分为带排序的部分
    对后部分进行逐个选取，进行比较插入到前部分，完成插入排序

usage:
os: Mac
code style: pep8

process sort:

source: 19  30  28  7  20

target:
    [19]  30  28  7  20
    [19  30]  28  7  20
    [19  28  30]  7  20
    [7  19  28  30]  20
    [7  19  20  28  30]

"""

__version__ = "v.1.0"
__author__ = "PyGo"
__time__ = "2017/5/27"
__mail__ = "gaomingliang971366@163.com"


def charu(alist):
    max = len(alist)
    for i in range(1, max):
        key = alist[i]
        j = i - 1
        # 对前排序部分进行插入
        while j >= 0:
            if alist[j] > key:
                alist[j + 1], alist[j] = alist[j], key
            j -= 1
    return alist

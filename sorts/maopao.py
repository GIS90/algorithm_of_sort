# -*- coding: utf-8 -*-


"""
describe:

冒泡排序
时间复杂度不可以预计，跟数据的本身有很大关系
但是，不建议用此排序，耗时大并且跟数据本身质量有关

算法思想：
    对所有的数据进行一次所有的遍历
    在遍历当前的元素时，对当前元素之后的数据进行比较，并且比较的方式两两比较，符合条件进行交换，
    其交换的方式就像气泡一样，向上升起，得名冒泡排序算法
    

usage:
os: Mac
code style: pep8
process sort:

source: 19  30  28  7  20
    
target:
        7  30  28  19  20
        7  28  30  19  20
        7  19  30  28  20
        7  19  28  30  20
        7  19  20  30  28
        7  19  20  28  30
        
"""

__version__ = "v.1.0"
__author__ = "PyGo"
__time__ = "2017/5/28"
__mail__ = "gaomingliang971366@163.com"


def maopao(alist):
    max = len(alist)

    for i in range(0, max):
        # 元素比较
        for j in range(i + 1, max):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]

    return alist

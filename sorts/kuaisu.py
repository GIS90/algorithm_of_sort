# -*- coding: utf-8 -*-


"""
describe: 个人认为快速排序的算法比较优秀，排序过程可以与分布式进行排序进行结果，
          当子节点陪许后，将结果返回当前子节点的父节点，逐级返回最终返回分布式结果进行统一结果的排序，
          每个节点只需要记录当前节点的排序比较分割标志位即可。

快速排序 
思路：
    输入列表
    1⃣️ 对列表进行选取一个标志位，选取大于标志位的数据放在标志位的右边，
    选取小于标志位的数据放在标志位的左边（循环left < right条件的方式）
    2⃣️ 按照 1⃣️ 方法对划分的2部分数据依次递归遍历，直到数据只剩2个元素进行比较排序
    3⃣️ 递归返回数据，顺序为 ⬅️ 🀄️ ➡️ 
    
    


usage:
code style: PEP8
os: Mac

process sort:
    len() 为奇数
    source: 23  19  25  35  20
    target:
    key = 23 (0 - 4)
        20  19  25  35  20
        20  19  25  35  25
        20  19  23  35  25
        left = right = 2
    key = 19 (0 - 1)
        19  20  
    key = 35 (3 - 4)
        19  20  
    
       
    len() 为偶数
    source: 23  19  25  35  20  21
    target:
    key = 23 (0 - 5)
        21  19  25  35  20  21
        21  19  25  35  20  25
        21  19  20  35  20  25
        21  19  20  35  35  25
        21  19  20  23  35  25
    key = 21 (0 - 2)    
        20  19  20 
        20  19  21
    key = 20 (0 - 1)
        19  20
    key = 35 (4 - 5)
        25 35
        
    组合左 中 右   
     
"""

__version__ = "v.1.0"
__author__ = "PyGo"
__time__ = "2017/5/24"
__mail__ = "gaomingliang971366@163.com"


def kuaisu(alist, left, right):

    if left >= right:
        return alist

    key = alist[left]
    low = left
    high = right
    # print "alist: %s, left: %d, right: %d" % (alist, left, right)

    while left < right:
        # 排序数据右部分
        while left < right and alist[right] >= key:
            right -= 1
            # print 'while ------- right: %d, alist[right]: %d, alist: %s, key: %d' % (right, alist[right], alist, key)
        alist[left] = alist[right]
        # print 'while right: %d, alist: %s' % (right, alist)

        # 排序数据左部分
        while left < right and alist[left] <= key:
            left += 1
            # print 'while +++++++ left: %d, alist[left]: %d, alist: %s, key: %d' % (left, alist[left], alist, key)
        alist[right] = alist[left]
        # print 'while left: %d, alist: %s' % (left, alist)

    if left == right:
        alist[left] = key
    # print alist
    # print "********************************"
    kuaisu(alist, low, left - 1)
    kuaisu(alist, left + 1, high)

    return alist

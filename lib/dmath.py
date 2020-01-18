#!/usr/bin/env python
# dMath - a simple math and not-math extension
import math

# 数组内数据的平均值 Average
def avg(arr):
    __avg_val = sum(arr) / len(arr)
    return __avg_val

def __cov(arr1, arr2):
    __avg1 = avg(arr1)
    __avg2 = avg(arr2)
    pass

# 计算方差（内部方法） Variance
def __varc(arr, sam):
    __dev = 0
    __avg = avg(arr)
    __len = len(arr) - sam
    for __num in arr:
        __dev += math.pow(__num - __avg, 2)
    __result = __dev / __len
    return __result

# 数组中数据的总体方差 DVariance
def dvar(arr):
    return __varc(arr, 0)

# 数组中数据的样本方差 SVariance
def svar(arr):
    return __varc(arr, 1)

# 数组中数据的标准差（均方差） Standard Deviation
def stddevd(arr):
    return math.sqrt(dvar(arr))

def stddevs(arr):
    return math.sqrt(svar(arr))

# 从数组中指定筛选元素
def each(arr, begin, count):
    __each_content = []
    __i = 0
    while 1:
        __list_id = begin + count * __i
        if __list_id < len(arr):
            __each_content.append(arr[__list_id])
            __i += 1
        else:
            break
    return __each_content


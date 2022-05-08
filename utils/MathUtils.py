"""
@Project: 软件构造课设
@Description: 用于chart的数学工具类
@Time:2022/4/22
@Author:WYW

"""
import numpy as np


def get_min_array(X):
    """
    返回全部是最小值的数组
    :param X: 需要获取最小值的数组
    :return: 长度和 param：X 一致的全为最小值的数组
    """
    min_val = np.min(X)
    min_array = [min_val for i in range(len(X))]
    return min_array


def get_max_array(X):
    """
    返回全部是最大值的数组
    :param X: 需要获取最大值的数组
    :return: 长度和 param：X 一致的全为最大值的数组
    """
    max_val = np.max(X)
    max_array = [max_val for i in range(len(X))]
    return max_array


def get_diff_array(X):
    """
    返回差值数组，计算两个元素之间的差值
    :param X: 需要计算差值的数组
    :return: 差值数组，长度为 param：X的长度减1。
    """
    diff_array = [X[i + 1] - X[i] for i in range(len(X) - 1)]
    return diff_array

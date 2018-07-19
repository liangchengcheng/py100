#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出了第10个斐波那契数列
print fib(10)


# 使用递归
def fib1(n):
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


# 输出了第10个斐波那契数列
print fib1(10)


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def fib2(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 输出前 10 个斐波那契数列
print fib2(10)
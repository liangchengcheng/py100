#!/usr/bin/python
# -*- coding: UTF-8 -*-

Tn = 0
Sn = []
n = int(raw_input('n = '))
a = int(raw_input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x, y: x + y, Sn)
print "计算和为：", Sn
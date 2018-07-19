#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

myD = {1: 'a', 2: 'b', 3: 'c'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1)  # 暂停一秒

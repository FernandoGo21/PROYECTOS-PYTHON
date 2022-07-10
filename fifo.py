# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:19:39 2020

@author: User
"""

import queue

q = queue.Queue()

for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:34:20 2018

@author: ptbngoc
"""

import numpy as np

def binary_search(list_values, x):
    pos = -1
    middle = len(list_values) / 2
    
    for i in range(0, int(middle)):
        if list_values[i] == x:
            pos = i
            return pos
    for i in range(int(middle), len(list_values)):
        if list_values[i] == x:
            pos = i
            return pos
    
    return pos
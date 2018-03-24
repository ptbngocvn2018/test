#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:42:52 2018

@author: ptbngoc
"""

import numpy as np
import unittest
import binary_search as bs

class BinarySearchTest(unittest.TestCase):
    def test_binary_search(self):
        list_values = [1,3,5,6,8,10]
        pos = bs.binary_search(list_values, 6)
        self.assertEqual(pos, 3)

if __name__ == '__main__':
    unittest.main()
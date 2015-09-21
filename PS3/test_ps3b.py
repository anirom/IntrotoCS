# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Test del modulo ps3b

import unittest
from ps3b import subStringMatchExact

class countString(unittest.TestCase):

    def test_subStringMatchExact(self):
        res = subStringMatchExact("attgcacgttgattgacttca","ttg")
        self.assertEqual(res,(1,8,12))
        res = subStringMatchExact("attgcacgttgattgacttca","ttga")
        self.assertEqual(res,(8,12))

if __name__ == '__main__':
    unittest.main()
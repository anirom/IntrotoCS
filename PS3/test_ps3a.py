# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Matching strings: a biological perspective

# Test del modulo ps3a

import unittest
from ps3a import countSubStringMatch, countSubStringMatchRecursive

class countString(unittest.TestCase):

    def test_countSubStngMatch(self):
        res = countSubStringMatch("attgcacgttgattgacttca","ttg")
        self.assertEqual(res,3)

    def test_countSubStringMatchRecursive(self):
        res = countSubStringMatchRecursive("attgcacgttgattgacttca","ttg")
        self.assertEqual(res,3)

if __name__ == '__main__':
    unittest.main()



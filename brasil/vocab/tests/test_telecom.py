# -*- coding:utf-8 -*-
import unittest


class DDDUnitTests(unittest.TestCase):

    def test_ddd(self):
        from brasil.vocab.telecom import ddd
        self.assertEqual(len(ddd), 67)
        self.assertEqual(ddd[0][0], '11')
        self.assertEqual(ddd[0][1], '11')


class CNGUnitTests(unittest.TestCase):

    def test_cng(self):
        from brasil.vocab.telecom import cng
        self.assertEqual(len(cng), 4)
        self.assertEqual(cng[0][0], '0300')
        self.assertEqual(cng[0][1], '0300')


class CodesUnitTests(unittest.TestCase):

    def test_codes(self):
        from brasil.vocab.telecom import codes
        self.assertEqual(len(codes), 71)
        self.assertEqual(codes[0][0], '11')
        self.assertEqual(codes[0][1], '11')
        self.assertEqual(codes[-1][0], '0900')
        self.assertEqual(codes[-1][1], '0900')

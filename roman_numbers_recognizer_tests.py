#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from roman_numbers_recognizer import RomanNumbersRecognizer

class TestRomanNumberRecognizer(unittest.TestCase):
    def setUp(self):
        self.recognizer = RomanNumbersRecognizer()

    def test_shuffle(self):
        self.assertEqual(self.recognizer.recognize('I'), 1)
        self.assertEqual(self.recognizer.recognize('II'), 2)
        self.assertEqual(self.recognizer.recognize('III'), 3)
        self.assertEqual(self.recognizer.recognize('IV'), 4)
        self.assertEqual(self.recognizer.recognize('V'), 5)
        self.assertEqual(self.recognizer.recognize('VI'), 6)
        self.assertEqual(self.recognizer.recognize('VII'), 7)
        self.assertEqual(self.recognizer.recognize('VIII'), 8)
        self.assertEqual(self.recognizer.recognize('IX'), 9)
        self.assertEqual(self.recognizer.recognize('X'), 10)
        self.assertEqual(self.recognizer.recognize('XI'), 11)
        self.assertEqual(self.recognizer.recognize('XII'), 12)
        self.assertEqual(self.recognizer.recognize('XIII'), 13)
        self.assertEqual(self.recognizer.recognize('XIV'), 14)
        self.assertEqual(self.recognizer.recognize('XV'), 15)
        self.assertEqual(self.recognizer.recognize('XVI'), 16)
        self.assertEqual(self.recognizer.recognize('XVII'), 17)
        self.assertEqual(self.recognizer.recognize('XVIII'), 18)
        self.assertEqual(self.recognizer.recognize('XIX'), 19)
        self.assertEqual(self.recognizer.recognize('XX'), 20)
        self.assertEqual(self.recognizer.recognize('XXX'), 30)
        self.assertEqual(self.recognizer.recognize('XL'), 40)
        self.assertEqual(self.recognizer.recognize('L'), 50)
        self.assertEqual(self.recognizer.recognize('LX'), 60)
        self.assertEqual(self.recognizer.recognize('LXX'), 70)
        self.assertEqual(self.recognizer.recognize('LXXX'), 80)
        self.assertEqual(self.recognizer.recognize('XC'), 90)
        self.assertEqual(self.recognizer.recognize('C'), 100)
        self.assertEqual(self.recognizer.recognize('CC'), 200)
        self.assertEqual(self.recognizer.recognize('CCC'), 300)
        self.assertEqual(self.recognizer.recognize('CD'), 400)
        self.assertEqual(self.recognizer.recognize('D'), 500)
        self.assertEqual(self.recognizer.recognize('DC'), 600)
        self.assertEqual(self.recognizer.recognize('DCC'), 700)
        self.assertEqual(self.recognizer.recognize('DCCC'), 800)
        self.assertEqual(self.recognizer.recognize('CM'), 900)
        self.assertEqual(self.recognizer.recognize('M'), 1000)
        self.assertEqual(self.recognizer.recognize('MM'), 2000)
        self.assertEqual(self.recognizer.recognize('MMM'), 3000)
        self.assertEqual(self.recognizer.recognize('XIVV'), None)
        self.assertEqual(self.recognizer.recognize('VIIII'), None)
        self.assertEqual(self.recognizer.recognize('LL'), None)
        self.assertEqual(self.recognizer.recognize('CDD'), None)
        self.assertEqual(self.recognizer.recognize('DCCCC'), None)
        self.assertEqual(self.recognizer.recognize('MMMM'), None)

if __name__ == '__main__':
    unittest.main()

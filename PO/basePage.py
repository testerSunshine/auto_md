# -*- coding: utf8 -*-
import unittest
from PO.equalScreenshot import myequal
from PO.myDriver import myDriver
from common.base_login import Login
from PO.warp import testcase
import os
import time

# class Base(unittest.TestCase, myequal, Login):
class Base(unittest.TestCase, Login):

    def setUp(self):
        self.driver = myDriver.get_driver()
        self.start_app()

    def tearDown(self):
        self.driver.quit()

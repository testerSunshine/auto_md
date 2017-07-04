# -*- coding: utf8 -*-
__author__ = 'Alex.xu'
class MyAssertionError(AssertionError):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        if self.msg is not None:
            exception_msg = "MyAssertionError Message: %s\n" % self.msg
            return exception_msg

class MyException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        if self.msg is not None:
            exception_msg = "MyException Message: %s\n" % self.msg
            return exception_msg
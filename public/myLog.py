# -*- coding: utf8 -*-
import logging
import os
import time
import logging.handlers
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
now = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class GetMyLog():
    def createFile(self):
        runpath = os.getcwd()
        logFile = os.path.abspath(os.path.join(runpath, 'Result', day, "steps"))
        if os.path.exists(logFile):
            self.filename = os.path.normcase(logFile + '/' + 'setps.log')
            return self.filename
        else:
            os.makedirs(logFile)
            self.filename = os.path.normcase(logFile + '/' + 'setps.log')
            return self.filename

    def myLog(self):
        '''
        调取log
        :return: logger
        '''
        LOG_FILE = self.createFile()
        self.handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
        self.fmt = '%(asctime)s - %(name)s -%(levelname)s -%(message)s'
        self.formatter = logging.Formatter(self.fmt)  # 实例化formatter
        self.handler.setFormatter(self.formatter)  # 为handler添加formatter
        self.logger = logging.getLogger('test_steps')
        self.logger.addHandler(self.handler)  # 为logger添加handler
        self.logger.setLevel(logging.DEBUG)
        return self.logger

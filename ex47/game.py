# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 用来被测试的代码

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)
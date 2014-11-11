# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from collections import namedtuple

LineInfo = namedtuple(
    'LineInfo',
    ['filename', 'line', 'col']
)

class ModelBase(object):
    line_info = None
                
class Rule(ModelBase):

    def __init__(self, name, conditions, actions):
        self.name = name
        self.conditions = conditions
        self.actions = actions

class Condition(ModelBase):
    def __init__(self, test, repeat, within):
        self.test = test
        self.repeat = repeat
        self.within = within

class Comparison(ModelBase):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

class BoolOperation(ModelBase):
    def __init__(self, operator, args):
        self.operator = operator
        self.args = args

class Action(ModelBase):
    def __init__(self, id, args):
        self.id = id
        self.args = args
        





















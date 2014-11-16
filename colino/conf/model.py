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

class Configuration(ModelBase):
    """The root node of the configuration"""
    
    def __init__(self, rules):
        self.rules = rules

    def __repr__(self):
        return "Configuration(rules=%s)" % repr(self.rules)
        
class Rule(ModelBase):

    def __init__(self, name, conditions, actions):
        self.name = name
        self.conditions = conditions
        self.actions = actions

    def __repr__(self):
        return "Rule(%s, %s, %s)" % \
            ( repr(self.name), repr(self.conditions), repr(self.actions) )

class Condition(ModelBase):
    def __init__(self, test, repeat, within):
        self.test = test
        self.repeat = repeat
        self.within = within

    def __repr__(self):
    
        return "Condition(%s, repeat=%s, within=%s)" % \
            ( repr(self.test), repr(self.repeat), repr(self.within) )

        
class Comparison(ModelBase):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return "Comparison(%s, %s, %s)" % \
            ( repr(self.operator), repr(self.left), repr(self.right))

        
class BoolOperation(ModelBase):
    def __init__(self, operator, *args):
        self.operator = operator
        self.args = args

    def __repr__(self):
        return "BoolOperation(%s, %s)" % \
            ( repr(self.operator), repr(self.args))

        
class Action(ModelBase):
    def __init__(self, id, args):
        self.id = id
        self.args = args
    
    def __repr__(self):
        return "Action(%s, %s)" % \
            ( repr(self.id), repr(self.args))

   




















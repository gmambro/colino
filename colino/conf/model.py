# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

class Rule(object):

    def __init__(self, name, conditions, actions):
        self.name = name
        self.conditions = conditions
        self.actions = actions

    def __repr__(self):
        return "Rule(name=%s, conditions=%s, actions=%s)" % \
               (repr(self.name), repr(self.conditions), repr(self.actions))





















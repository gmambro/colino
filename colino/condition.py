from __future__ import (absolute_import, division,
    print_function, unicode_literals)

class Condition(object):

    def __init__(self, condition_model):
        # used for holding objects like compiled reges
        self.init_context = {}
        # variables referenced by condition
        self.variables = set()
        # the condition python code
        self.code = self.compile(condition_model)
    
    def compile(self, condition_model):
        """create a valid python expression from a condition model"""
        # TODO recursice descent into model, one method for class
        pass

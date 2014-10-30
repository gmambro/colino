# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import colino.digraph


class Condition(object):
    
    def evaluate(self, context, event):
        """return true or false"""
        raise NotImplemented

class RuleNode(digraph.Node):

    def __init__(self, time_limit):       
        super(Node, self).__init__()
        self.time_limit = time_limit

        # last edge status used to implement repetition rules
        self.last_edge = None
        self.last_edge_count = 0

    def update_last_edge(self, edge):
        if self.last_edge == edge:
            self.last_edge_count += 1
        else:
            self.last_edge = edge
            self.last_edge_count = 1

class StartRuleNode(digraph.Node):
    pass

class AcceptRuleNode(digraph.Node):
    pass

class RejectRuleNode(digraph.Node):
    pass
            
class RuleEdge(digraph.Edge):
    def __init__(self, condition, threshold):
        self.condition = condition
        self.threshold = threshold
        
class RuleGraph(digraph.DiGraph):
    def __init__(self):
        self.start = 
        self.accept_rule_node = 

            
                








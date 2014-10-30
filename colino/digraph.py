# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

class BaseNode(object):
    pass
        
class Edge(object):
    def __init__(self, node1, node2)
        self.node1 = node1
        self.node2 = node2

class DiGraph(object):

    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self._outgoing = {}
        self._ingoing = {}     

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, edge):
        node1 = edge.node1
        node2 = edge.node2          
        if not node1 in self.nodes:
            raise ValueError
        if not node2 in self.nodes:
            raise ValueError
        
        self.edges.add(edge)
        self._outgoing.set_default(node1, []).append(node2)
        self._ingoing.set_default(node2, []).append(node1)
        
    def get_out_edges(self, node):
        return self._outgoing.get(node, [])

    def get_in_edges(self, node):
        return self._ingoing.get(node, [])
        

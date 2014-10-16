class Condition(object):
    
    def evaluate(self, context, event):
        raise NotImplemented

class Node(object):

    def __init__(self, time_limit):
        self.time_limit = time_limit
        
class Edge(object):

    def __init__(self, node1, node2, condition, threshold=0):
        self.condition = condition
        self.node1 = node1
        self.node2 = node2
        self.threshold = threshold            
            
                
class RuleGraph(object):

    def __init__(self):
        self.nodes = []
        self.edges = []
        self.start = Node()
        self.end = Node()
        

class EdgeStatus(object):

    def __init__(self, edge):
        self.edge = edge
        self.count = count
        
        
class GraphStatus(object):

    def __init__(self, graph):
        self._current_node = graph.start  
        self._edge_status = None
        self._context = {}
        self._start_time = None

    def evaluate(self, event):
        # check all current edge status
        # TODO
        # check all outgoing edges
        # TODO
        pass



# RULE 1
#  <c1>;
#  <c2> WITHIN t
#
# graph with time goals
# 
#   (start)--c1-->( s1 )--c2-->( end, t)
#
# graph with expires
#
#   (start)--c1-->( s1, t )--c2-->( end )
#
# RULE 2
#  <c1>;
#  <c2> WITHIN t1;
#  <c3> WITHIN t2
#
# graph with time goals
#
#    (start)--c1-->( s1 )--c2->( s2, t1 )--c3-->( end, t1 + t2 )
#
# graph with expires
#    (start)--c1-->( s1, t1 )--c2->( s2, t1 + t2 )--c3-->( end )
#
# RULE 3
#  <c1>;
#  <c2> OR <c3> WITHIN t
#
#  graph with time goals
#
#                         / c2 \
#                        /      \
#    (start)--c1-->( s1 )        ->( end, t1 + t2 )
#                        \      /
#                         \ c3 /
#

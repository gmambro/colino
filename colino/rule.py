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
        

class Predicate(object):

    def __init__(self, time_constraint=None):
        self._constraint=None
    
    def evaluate(self, context, event):
        raise NotImplemented
    


class Rule(object):

    def __init__(self):
        self._predicates = set()


class RuleBinding(object):

    def __init__(self, rule):
        self._rule = rule 

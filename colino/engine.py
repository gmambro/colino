from event import Event


class EdgeStatus(object):
    """Used by RulePartialMatch to implement repetition rules."""
    
    def __init__(self, edge):
        self.edge = edge
        self.count = count
        
        
class RulePartialMatch(object):
    """A potential match of a rule.

    Mantains the current status in the rule
    associated graph, the current context values and time informations.
    """
   
    def __init__(self, graph):
        self.graph = graph
        self.rule = graph.rule
        
        self._current_node = graph.start
        self._edge_status = None
        self._context = {}
        self._start_time = None


   @classmethod
   def bootstrap(cls, graph, event):
       """Return a new RulePartialMatch if the event can start a rule match"""

    def eat_event(self, event):
        """Consume an event, return true if status has changed."""
        
        # TODO check all current edge status

        # TODO check all outgoing edges

        pass

    def accepted():
        """Returns true if it's in a acceptance state (action should be triggered)""" 
        
        pass

    def active():
        """Return true if it's in a non-final state"""
        pass
    
class EventEngine(object):
    
    
    _rule_graphs = []
    _rule_status = []

    # TODO prepare pre initialized rule_status
    
    def process(self, event):
        """Feed the event to all the rules and trigger any matching action"""
        
        rule_status = self._rule_status
        for s in rule_status:
            if s.evaluate(event):

                if s.eat_event():
                    self.run_action(s.get_rule())

        for g in _rule_graphs:
            status = RuleStatus(graph)
            if graph.eat_event(event):
                rule_status.append(status)

        self._rule_status = [ s for s in rule_status if not s.active() ]
                
        
        















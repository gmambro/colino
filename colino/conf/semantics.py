# -*- coding: utf-8 -*-


from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


class SemanticCheck(object):
    """Traverse a model and preform consistency checks"""

    def __init__(self):
        self._errors = []
    
    def check_conditions(self, conditions):        
        if len(conditions) > 1:
            for cond in conditions[1:]:
                if cond.within is None:
                    print("error in ",cond.line_info)
                    raise SemanticError("chained condition without time contraint",
                                        cond.line_info)
                else:
                    print(cond.within)










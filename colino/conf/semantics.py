# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from colino.conf.model import Rule

class ColinoSemantics(object):

    ## def ESC(self, ast):
    ##    return ast
    
    def STRING(self, ast):
        return "".join(ast)
    
	## def INTEGER(self, ast):
	## 	pass
    
	## def REGEX(self, ast):
	## 	pass
    
    ## def FRAGMENT(self, ast):
    ##  return ast   
    
	## def action(self, ast):
	## 	pass
    
	## def action_list(self, ast):
	## 	pass
    
	## def and_test(self, ast):
	## 	pass
    
	## def comp_op(self, ast):
	## 	pass
    
	## def comparison(self, ast):
	## 	pass
    
	## def condition(self, ast):
	## 	pass
    
	## def condition_list(self, ast):
	## 	pass

    ## def configuration(self, ast):
	## 	pass

    ## def expr(self, ast):
	## 	pass

    ## def identifier(self, ast):
	## 	pass

    ## def not_test(self, ast):
	## 	pass

    ## def or_test(self, ast):
	## 	pass

    def rule(self, ast):
        return Rule(ast['name'], ast['conditions'], ast['actions'])
    
	## def test(self, ast):
	## 	pass


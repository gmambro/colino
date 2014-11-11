from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from colino.conf.grako import colinoParser
from colino.conf.model import *
   

class ModelBuilder(object):

    def _add_line_info(Self, model, ast):
        """Set model.LineInfo from a grako ast"""
        line_info = ast.parseinfo.buffer.line_info()
        model.line_info = LineInfo(
            line_info.filename,
            line_info.line,
            line_info.col)
        return model
    
    def __init__(self):
        self._identifier = {}
                
    def ESC(self, ast):
        return ast.decode('string_escape')
    
    def STRING(self, ast):
        return "".join(ast)
    
    def INTEGER(self, ast):
        return int(ast)
    
    def REGEX(self, ast):
     	return ast

    def IDENTIFIER(self, ast):
        return ast
    
    def identifier(self, ast):
        return ast   
    
    def action(self, ast):
        return Action(ast, [])

    def and_test(self, ast):
        if len(ast) == 1:
            return ast
        else:
            BoolOperation('and', ast[0], ast[2])


    def or_test(self, ast):
        if len(ast) == 1:
            return ast
        else:
            return BoolOperation('or', ast[0], ast[2])
    
    def not_test(self, ast):        
        if ast['not'] is not None:
            return BoolOperation('not', ast['not'])
        else:
            return ast.comparison
    
    def comp_op(self, ast):
        return ast
    
    def comparison(self, ast):
        model = Comparison(ast.op, ast.left, ast.right)
        self._add_line_info(model, ast)
        return model

    def time_limit(self, ast):
        """return time limit as seconds"""

        if ast.unit == 's':
            return ast.value
        if ast.unit == 'm':
            return ast.value * 60
        if ast.unit == 'h':
            return ast.value  * 3600
        assert(False)

    def test(self, ast):
        return ast
    
    def condition(self, ast):
        model = Condition(ast.test, ast.repeat, ast.within)
        self._add_line_info(model, ast)
        return model

    def configuration(self, ast):
        return ast

    def action_list(self, ast):
        return ast
    
    def expr(self, ast):
        return ast

    def rule(self, ast):        
        model = Rule(ast.name, ast.conditions, ast.actions)
        self._add_line_info(model, ast)
        return model

        
    def test(self, ast):
        return ast


class ConfLoader(object):

    start_symbol = 'configuration'
    
    def load(self, filename):        
        parser = colinoParser(parseinfo=True)
        semantics = ModelBuilder()

        with open(filename, 'r') as f:
            text = f.read()

        conf = parser.parse(text,
                            self.start_symbol,
                            filename=filename,
                            semantics=semantics)
                    
        return conf

















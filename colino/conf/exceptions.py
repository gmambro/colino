from __future__ import (absolute_import, division, print_function,
                        unicode_literals)



class ConfigurationException(Exception):
    def __init__(self, message, lineinfo):
        self.message = message
        self.lineinfo = lineinfo

    def __str__(self):
        l = self.lineinfo
        return "%s:%d:%d:%s" % ( l.filename, l.line, l.col, self.message)

    
class SyntaxError(ConfigurationException):
    pass
   
        
class SemanticError(ConfigurationException):
    pass

















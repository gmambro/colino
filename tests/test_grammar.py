import unittest
from colino.conf.loader import colinoParser, ModelBuilder

# for debugging
import pprint

class GrammarTests(unittest.TestCase):

    trace = False
    pp = pprint.PrettyPrinter(indent=4)
        
    def setUp(self):
        self.parser = colinoParser(parseinfo=True)
        self.semantics = ModelBuilder()
    
    def parse(self, text, *args):
        ast = self.parser.parse(text,
                                semantics=self.semantics,
                                trace=self.trace,
                                *args)
        if self.trace:
            print "Text: ", text
            print "Model :"
            self.pp.pprint(ast)
        return ast

    def test_identifier(self):
        ast = self.parse("pippo123", "IDENTIFIER")
        self.assertIsNotNone(ast)
        
    def test_escape(self):
        ast = self.parse(r"\t", "ESC")
        self.assertEqual(ast, u"\t")

    def test_escaped_string(self):
        ast = self.parse(r" 'abc\n\t' ", "STRING")
        self.assertEqual(ast, u"abc\n\t")
                
    def test_simple_rule(self):
        text = '''
           rule test
              match msg = 'hello'
              action nil
           end
        '''
        ast = self.parse(text, 'configuration')

    def test_identifier(self):
        for i in [ 'a', 'aa', 'a1', 'abc' ]:
            ast = self.parse(i, 'IDENTIFIER')
            self.assertEqual(ast, i)
                
    def test_scoped_identifier(self):
        for i in [ 'a.b', 'aa.b', 'aa.bb',
                   'a.b.c', 'aa.bb.cc', 'a1.v2.c3' ]:
            ast = self.parse(i, 'SCOPED_IDENTIFIER')
            self.assertEqual(ast, i)
            
    def test_condition_list(self):
        text = '''
           rule test
              match msg = 'hello'
              match msg = 'world'
              action nil
           end
        '''
        ast = self.parse(text, 'configuration')

                    
    def test_condition_regex(self):
        text = '''
              match msg ~ /\w+=\w+/
        '''
        ast = self.parse(text, 'condition')

    def test_and_test(self):
        text = '''
         a = 'a' and b = 'b' and c = 'c'
        '''  
        ast = self.parse(text, 'and_test')
        self.assertEqual(len(ast.args), 3)

    def test_or_test(self):
        text = '''
        a = 'a' or b = 'b' or c = 'c'
        '''
        ast = self.parse(text, 'or_test')
        self.assertEqual(len(ast.args), 3)
             
    def test_within_rule(self):
        text = '''
              match within 4s msg = 'hello' 
        '''
        ast = self.parse(text, 'condition')
        
        
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(GrammarTests)

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'trace':
        GrammarTests.trace = True

    unittest.TextTestRunner(verbosity=2).run(suite())

if __name__ == '__main__':
    main()

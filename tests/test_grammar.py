import unittest
from colino.conf.parser import colinoParser
from colino.conf.semantics import ColinoSemantics


class GrammarTests(unittest.TestCase):

    def setUp(self):
        self.parser = colinoParser()
        self.semantics = ColinoSemantics()
        
    def tearDown(self):
        import json
        print("AST")
        print(self.ast)
        print("")

    def parse(self, text, *args):
        self.ast = self.parser.parse(text,
                                     semantics=self.semantics,
                                    # trace=True,
                                     *args)

    def test_escape(self):
        self.parse(r"\t", "ESC")
                
    def test_simple_rule(self):
        text = '''
           rule test
              match msg = 'hello'
              action nil
           end
        '''
        self.ast = self.parser.parse(text, 'configuration')

    def test_condition_list(self):
        text = '''
           rule test
              match msg = 'hello';
              match msg = 'world'
              action nil
           end
        '''
        self.parse(text, 'configuration')

                    
    def test_regex_condition(self):
        text = '''
              match msg ~ /\w+=\w+/
        '''
        self.parse(text, 'condition')
        
     
    def test_within_rule(self):
        text = '''
           rule test
              match msg = 'hello' within 4s
              action nil
           end
        '''
        self.parse(text, 'configuration')

        
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(GrammarTests)

def main():
    unittest.TextTestRunner(verbosity=2).run(suite())

if __name__ == '__main__':
    main()

import unittest
from colino.conf.parser import colinoParser

class GrammarTests(unittest.TestCase):

    def setUp(self):
          # TODO
        self.parser = colinoParser()
    
    def test_simple_rule(self):
        text = '''
           rule test
              match msg = 'hello'
              action nil
           end
        '''
        print self.parser.parse(text, 'configuration')

    def test_condition_list(self):
        text = '''
           rule test
              match msg = 'hello';
              match msg = 'world'
              action nil
           end
        '''
        print self.parser.parse(text, 'configuration')
  

              
    def test_regex_condition(self):
        text = '''
              match msg ~ /\w+=\w+/
        '''
        print self.parser.parse(text, 'condition')
        
      


        
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(GrammarTests)

def main():
    unittest.TextTestRunner(verbosity=2).run(suite())

if __name__ == '__main__':
    main()

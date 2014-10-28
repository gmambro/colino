Events
------

An event is described a set of attribute-value pairs.
Timestamp and message are required, other attributes can be added by a specific event source or by a parsing rule.


Sources
-------

A source can be a file, a socket, or a pipeline.

Channels
--------

Channels defines a stream of events.  A channel can be fed from a source o from
other channels and can filter events.
   

Rules
-----

A rule describes a pattern of conditions that will lead to an action.
A condition is a set of tests on attributes with an optional time or
repetition constraint

Syntax::
 rule ::= "rule"  condition_list "action" action_list

 condition ::=  'match' test [ [ 'repeated' INTEGER 'times' ] 'within' time_limit ] 

  test ::=   test 'or' test
           | test 'and' test
	   | 'not' test
	   | identifier comp_operator expression
           | '~'   regex
           | '!~'  regex

  comp_op  =  '<'  | '>'  | '='  | '>=' | '<='  | '!=' | 'in' | 'not' 'in'


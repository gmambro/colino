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

Conditions
----------

A condition is a set of tests on attributes.

condition =  condition_expr
condition_expr =  attribute_test  
                          '(' condition_expr ')'
                         | condition_expr or condition_expr
                         | condition_expr and condition_expr

attribute_test =  attribute comparison string
                         | attribute comparison int
                         | attribute comparison timestamp
                         | attribute '~' regex
                         | attribute 'in' timeinterval


Rules
-----

A rule describe a pattern of conditions that will lead to an action.

Syntax::
 rule = "rule", condition-chain, "action", action 
 condition-chain = condition, [repeat],  {  ';', condition, repeat within?) } 

 repeat =  "repeat" int

 within = "within" int ("s"|"m"|"h")

Sample rules and graph translations
===================================

Concatenation
-------------

::

 RULE 1
  <c1>;
  <c2> WITHIN t

graph with time goals::

 (start)--c1-->( s1 )--c2-->( end, t)

graph with expire time values i.e. node s1 should be left before t::

 (start)--c1-->( s1, t )--c2-->( end )


Expire time is the maximum of the time goals of all node successors::

 RULE 2
  <c1>;
  <c2> WITHIN t1;
  <c3> WITHIN t2

graph with time goals::

 ( start )--c1-->( s1 )--c2->( s2, t1 )--c3-->( end, t1 + t2 )

graph with expires::

 ( start )--c1-->( s1, t1 )--c2->( s2, t1 + t2 )--c3-->( end )


Disjunction
-----------

::

 RULE 3
   <c1>;
   <c2> OR <c3> WITHIN t

graph with time goals::

                       / c2 \
                      /      \
  (start)--c1-->( s1 )        ->( end, t1 + t2 )
                      \      /
                       \ c3 /


Repetition
----------

::

  RULE 4
    <c1> <n> TIMES WITHIN t

 (start)--c1,n-->( end, t )

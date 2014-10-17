Sample rules and graph translations

RULE 1
  <c1>;
  <c2> WITHIN t

graph with time goals

 (start)--c1-->( s1 )--c2-->( end, t)

graph with expires, i.e. node s1 should be left before t.
expire time is the maximum of the time goals of all node successors.

 (start)--c1-->( s1, t )--c2-->( end )

RULE 2
 <c1>;
 <c2> WITHIN t1;
 <c3> WITHIN t2

graph with time goals

( start )--c1-->( s1 )--c2->( s2, t1 )--c3-->( end, t1 + t2 )

graph with expires

( start )--c1-->( s1, t1 )--c2->( s2, t1 + t2 )--c3-->( end )

RULE 3
 <c1>;
 <c2> OR <c3> WITHIN t

graph with time goals
                       / c2 \
                      /      \
  (start)--c1-->( s1 )        ->( end, t1 + t2 )
                      \      /
                       \ c3 /


RULE 4
 <c1> <n> TIMES WITHIN t

 (start)--c1,n-->( end, t )

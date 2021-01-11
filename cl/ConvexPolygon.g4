grammar ConvexPolygon;

root : (asignment | color | myprint | area | perimeter | vertices | centroid | inside | equal | draw | operator  )  EOF;


vertex: REAL SPACE REAL;

convexpolygon : '[' (vertex (SPACE SPACE vertex)+) ']'
              | '[' vertex ']'
              ;

asignment : ID SPACE EQUAL SPACE convexpolygon
         | ID SPACE EQUAL SPACE operator
         ;

color : 'color ' ID COMA SPACE rgb ;

rgb  : '{' REAL SPACE REAL SPACE REAL '}';

myprint : 'print ' (operator |  TEXT  );

area : 'area ' operator ;

perimeter: 'perimeter ' operator ;

vertices : 'vertices ' operator ;

centroid : 'centroid ' operator ;

inside : 'inside ' operator  COMA SPACE operator ;

equal: 'equal ' operator COMA SPACE operator;

draw: 'draw ' '"' FILENAME '"' COMA SPACE( (operator (COMA SPACE operator)+) | operator);

operator: '(' operator ')'
        | operator ' * ' operator
        | operator ' + ' operator
        | '#' operator
        | '!' REAL
        | convexpolygon
        | ID
        ;

REAL: [0-9]+ '.'* [0-9]*;

EQUAL: ':=' ;

ID :  [a-zA-Z0-9] [a-zA-Z0-9]*;

COMA : ',';

SPACE : ' ';

FILENAME:  [a-zA-Z] [a-zA-Z0-9]* '.'[a-zA-Z]+;

TEXT: '"' CONTENT+  '"';

CONTENT: [a-z]
       | [A-Z]
       | '-'
       | '_'
       | SPACE
       | COMA
       ;

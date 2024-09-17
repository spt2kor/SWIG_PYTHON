#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./python/");

#for p in sys.path:
#    print( p )
import SimpleDS;

"""This is a 
        python script!"""

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python Data Structures and classes 2");

print ( nl, "******************************************** Print checkig module  SimpleDS \n" );
print ( nl," SimpleDS =  ", SimpleDS);
print ( nl," type(SimpleDS)  =  ", type(SimpleDS) );

print ( nl," dir(SimpleDS)  =  ", dir(SimpleDS) );

print ( nl, "******************************************** Print Macro SimpleDS.RED" );

print ( nl," SimpleDS.RED =  ", SimpleDS.RED , ", type( SimpleDS.RED ) =  ", type(SimpleDS.RED ) );

print ( nl, "******************************************** Print global variable SimpleDS.cvar.pi" );
print ( nl," SimpleDS.cvar =  ", SimpleDS.cvar);
print ( nl," type(SimpleDS.cvar)=  ", type(SimpleDS.cvar) );
print ( nl," dir (SimpleDS.cvar)=  ", dir (SimpleDS.cvar) );
print ( nl," SimpleDS.cvar.pi =  ", SimpleDS.cvar.pi);


print ( nl, "******************************************** Print global variable SimpleDS.cvar.some_no" );
print ( nl ," SimpleDS.cvar.some_no =  ", SimpleDS.cvar.some_no," type(SimpleDS.cvar.some_no) =  ", type(SimpleDS.cvar.some_no) );

print ( nl, "******************************************** Print global variable SimpleDS.calculateArea(10,20)" );
print ( nl," SimpleDS.calculateArea =  ", SimpleDS.calculateArea);
print ( nl," SimpleDS.calculateArea(10,20) =  ", SimpleDS.calculateArea(10,20));

#NOTE:  not working global char* , check global string, or check global char[]
print ( nl, "******************************************** Print global variable SimpleDS.cvar.class_name" );
print ( nl," SimpleDS.cvar =  ", SimpleDS.cvar.class_name);

print ( nl, "******************************************** Print checkig module  SimpleDS.Rectangle" );

print ( nl," SimpleDS.Rectangle =  ", SimpleDS.Rectangle);

print ( nl," type(SimpleDS.Rectangle)  =  ", type(SimpleDS.Rectangle) );

print ( nl," dir(SimpleDS.Rectangle)  =  ", dir(SimpleDS.Rectangle) );

print ( nl, "******************************************** Print using r1 = SimpleDS.Rectangle();" );

r1 = SimpleDS.Rectangle(10,20);
print ( nl," r1 =  ", r1);

#print ( nl," r1.this =  ", r1.this);
# AttributeError: 'SwigPyObject' object has no attribute 'this'

print ( nl," type(r1)=  ", type(r1) );

print ( nl, "******************************************** Print using r1.area();" );

print ( nl," r1.area() =  ", r1.area());

print ( nl, "******************************************** Print using r1.show();" );

print ( nl," r1.show() =  ", r1.show());

print ( nl, "******************************************** Print using r1.classInfo();" );

print ( nl," r1.classInfo() =  ", r1.classInfo());

print ( nl, "******************************************** Print using r1.thisown;" );

print ( nl," r1.thisown =  ", r1.thisown ) ;

print ( nl, "******************************************** Print using r2 = SimpleDS.Rectangle(r1);" );

r2 = SimpleDS.Rectangle(r1);
print ( nl," r2 =  ", r2);
    
r2.show();  

print ( nl, "******************************************** Print using r3 = r2.clone();" );

r3 = r2.clone();
print ( nl," r3 =  ", r3);
print ( nl," r3.area() =  ", r3.area());

r3.show(); 

print ( nl, "******************************************** r2.set(50,60);   " );
    
r2.set(50,60);      
r2.show();  

print ( nl, "******************************************** Rectangle& operator= (const Rectangle &other);  r3 = r2; " );
r3 = r2;  # NOTE : not working , as expected , instead of coying , its deleted the r3 previous object.

print ( nl," r3 =  ", r3);
r3.show(); 

print ( nl, "******************************************** Print using del r1, call DTOR;" );

del r1

print (nl, "********************************************");
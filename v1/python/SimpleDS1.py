#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
#sys.path.append('/path/to/directory')
sys.path.append("./generated_files/");
sys.path.append("./python/");

for p in sys.path:
    print( p )
    
import _SimpleDS;

"""This is a 
        python script!"""

nl = '[PYTHON CODE] : ';

print ( nl," Testing Basic Python Data Structures ");

print ( nl, "******************************************** Print checkig module  _SimpleDS" );
print ( nl," _SimpleDS =  ", _SimpleDS);
print ( nl," type(_SimpleDS)  =  ", type(_SimpleDS) );

print ( nl," dir(_SimpleDS)  =  ", dir(_SimpleDS) );

print ( nl, "******************************************** Print Macro _SimpleDS.RED" );

print ( nl," _SimpleDS.RED =  ", _SimpleDS.RED , ", type( _SimpleDS.RED ) =  ", type(_SimpleDS.RED ) );

print ( nl, "******************************************** Print global variable _SimpleDS.cvar.pi" );
print ( nl," _SimpleDS.cvar =  ", _SimpleDS.cvar);
print ( nl," type(_SimpleDS.cvar)=  ", type(_SimpleDS.cvar) );
print ( nl," _SimpleDS.cvar.pi =  ", _SimpleDS.cvar.pi);


print ( nl, "******************************************** Print global variable _SimpleDS.cvar.some_no" );
print ( nl ," _SimpleDS.cvar.some_no =  ", _SimpleDS.cvar.some_no," type(_SimpleDS.cvar.some_no) =  ", type(_SimpleDS.cvar.some_no) );

print ( nl, "******************************************** Print global variable _SimpleDS.calculateArea(10,20)" );
print ( nl," _SimpleDS.calculateArea =  ", _SimpleDS.calculateArea);
print ( nl," _SimpleDS.calculateArea(10,20) =  ", _SimpleDS.calculateArea(10,20));

#NOTE:  not working global char* , check global string, or check global char[]
#print ( nl, "******************************************** Print global variable _SimpleDS.cvar.class_name" );
#print ( nl," _SimpleDS.cvar =  ", _SimpleDS.cvar);
#print ( nl," _SimpleDS.cvar =  ", type(_SimpleDS.cvar) );
#print ( nl," _SimpleDS.cvar =  ", _SimpleDS.cvar.class_name);

print ( nl, "******************************************** Print checkig module  _SimpleDS.Rectangle" );

#print ( nl," _SimpleDS.Rectangle =  ", _SimpleDS.Rectangle);
'''        Traceback (most recent call last):
        File "/home/relman.ivcs/rajput/flow_arch_sandbox/FAST3_Python/v1/python/ds1.py", line 49, in <module>
        print ( nl," _SimpleDS.Rectangle =  ", _SimpleDS.Rectangle);
                                                ^^^^^^^^^^^^^^^^^^^
        AttributeError: module '_SimpleDS' has no attribute 'Rectangle'. Did you mean: 'new_Rectangle'?
        make: *** [ds1] Error 1         '''


#print ( nl," type(_SimpleDS.Rectangle)  =  ", type(_SimpleDS::Rectangle) );

#print ( nl," dir(_SimpleDS.Rectangle)  =  ", dir(_SimpleDS::Rectangle) );

print ( nl, "******************************************** Print using r1 = _SimpleDS.Rectangle();" );
#r1 = new _SimpleDS.Rectangle();
        #SyntaxError: invalid syntax
        #make: *** [ds1] Error 1

#r1 = _SimpleDS.Rectangle();
#AttributeError: module '_SimpleDS' has no attribute 'Rectangle'. Did you mean: 'new_Rectangle'?
#make: *** [ds1] Error 1

r1 = _SimpleDS.new_Rectangle(10,20);
print ( nl," r1 =  ", r1);

#print ( nl," r1.this =  ", r1.this);
# AttributeError: 'SwigPyObject' object has no attribute 'this'

print ( nl," type(r1)=  ", type(r1) );

print ( nl, "******************************************** Print using r1.area();" );
#print ( nl," r1->area() =  ", r1->area()); #SyntaxError: invalid syntax

#print ( nl," r1.area() =  ", r1.area());
        #AttributeError: 'SwigPyObject' object has no attribute 'area'
        #swig/python detected a memory leak of type 'Rectangle *', no destructor found.
        #3make: *** [ds1] Error 1
# del r1;  not working

print ( nl, "******************************************** Print using _SimpleDS.delete_Rectangle(r1);" );
_SimpleDS.delete_Rectangle(r1);

"""x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print(2+3)

print ( "17//3 = " , 17//3);
print ( "17%3 = " , 17%3);
print ( "5**3 = " , 5**3);

#print("_", _);
#NameError: name '_' is not defined

print('string \nline');
print("string \nline");
print(r'raw string \nline');

print(3 * '#' + ' Python' + 2*'!');

name = 'Python';
print (name[0] , name[-1] , name[2:5]);

#name[3] = "$";
#TypeError: 'str' object does not support item assignment
"""



print (nl, "********************************************");
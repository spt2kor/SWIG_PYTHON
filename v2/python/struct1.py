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

print ( nl, "******************************************** Print using r1 = SimpleDS.Algo();" );

r1 = SimpleDS.Algo(20);
print ( nl," r1 =  ", r1);


print ( nl," type(r1)=  ", type(r1) );

print ( nl, "******************************************** Print using r1.pri;" );

#print ( nl," r1.pri =  ", r1.pri);
#Traceback (most recent call last):
#  File "<>/FAST3_Python/v2/python/struct1.py", line 35, in <module>
#   print ( nl," r1.pri =  ", r1.pri);
#                              ^^^^^^
#AttributeError: 'Algo' object has no attribute 'pri'

print ( nl, "******************************************** Print using r1.pro;" );

#print ( nl," r1.pro =  ", r1.pro);
#Traceback (most recent call last):
#  File "<>/FAST3_Python/v2/python/struct1.py", line 44, in <module>
#    print ( nl," r1.pro =  ", r1.pro);
#                              ^^^^^^
#AttributeError: 'Algo' object has no attribute 'pro'


print ( nl, "******************************************** Print using r1.pub;" );

print ( nl," r1.pub =  ", r1.pub);
r1.pub = 20000; 
print ( nl," r1.pub =  ", r1.pub);

print ( nl, "******************************************** Print using r1.getPri();" );

print ( nl," r1.getPri() =  ", r1.getPri());

print ( nl, "******************************************** Print using r1.print();" );

#NOTE: print is python keyword, so we cannot use in our exported C++ interface class.

#print ( nl," r1.print() =  ", r1.print());
#Traceback (most recent call last):
#  File "<>/FAST3_Python/v2/python/struct1.py", line 64, in <module>
#    print ( nl," r1.print() =  ", r1.print());
#                                  ^^^^^^^^
#AttributeError: 'Algo' object has no attribute 'print'. Did you mean: '_print'?


print ( nl, "******************************************** Print using r1._print();" );

#NOTE: SWIG while compiling the print(), renamed it to _print(), and gave the warning below
# swig/../cpp/DataTypes.h:35: Warning 314: 'print' is a python keyword, renaming to '_print'
print ( nl," r1._print() =  ", r1._print());

print ( nl, "******************************************** Print using r1.classInfo();" );

print ( nl," r1.classInfo() =  ", r1.classInfo());

print ( nl, "******************************************** Print using r1.thisown;" );

print ( nl," r1.thisown =  ", r1.thisown ) ;

print ( nl, "******************************************** Print using r2 = SimpleDS.Algo(r1);" );

r2 = SimpleDS.Algo(r1);
print ( nl," r2 =  ", r2);
r2._print();  

print ( nl, "******************************************** Print using r3 = r2.clone();" );

r3 = r2.clone();
print ( nl," r3 =  ", r3);

r3._print(); 

print (nl, "***********  END OF PROGRAM *********************************");

















#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import SimpleDS;

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class Inheritance 1");

print ( nl, "********************************************  r1 = SimpleDS.Rectangle();" );

r1 = SimpleDS.Rectangle("Rect1",10,20);
print ( nl," r1 =  ", r1);
print ( nl," type(r1)=  ", type(r1) );

print ( nl, "******************************************** only derived func:non-virtual:  r1.area();" );

print ( nl," r1.area() =  ", r1.area());

print ( nl, "******************************************** overriden func:  r1.show();" );

print ( nl," r1.show() =  ", r1.show());

print ( nl, "******************************************** stati overriden func: r1.classInfo();" );

print ( nl," r1.classInfo() =  ", r1.classInfo());

#print ( nl," Rectangle.classInfo() =  ", Rectangle.classInfo());
#Traceback (most recent call last):
#  File "/home/relman.ivcs/rajput/flow_arch_sandbox/FAST3_Python/v2/python/inheritance1.py", line 31, in <module>
#    print ( nl," Rectangle.classInfo() =  ", Rectangle.classInfo());
#                                             ^^^^^^^^^
#NameError: name 'Rectangle' is not defined

print ( nl," SimpleDS.Rectangle.classInfo() =  ", SimpleDS.Rectangle.classInfo());

print ( nl, "******************************************** check ownership : r1.thisown;" );

print ( nl," r1.thisown =  ", r1.thisown ) ;


print ( nl, "******************************************** calling non-virtual func, only in base : r1.getName();" );

print ( nl," r1.getName() =  ", r1.getName() ) ;


print ( nl, "******************************************** calling non-virtual func, only in base : r1.privateFunc();" );

#r1.privateFunc();

#Traceback (most recent call last):
#  File "/home/relman.ivcs/rajput/flow_arch_sandbox/FAST3_Python/v2/python/inheritance1.py", line 44, in <module>
#    r1.privateFunc();
#    ^^^^^^^^^^^^^^
#AttributeError: 'Rectangle' object has no attribute 'privateFunc'


print ( nl, "******************************************** calling non-virtual func, only in base : r1.protctedFunc();" );

#r1.protctedFunc();

#Traceback (most recent call last):
#  File "/home/relman.ivcs/rajput/flow_arch_sandbox/FAST3_Python/v2/python/inheritance1.py", line 55, in <module>
#    r1.protctedFunc();
#    ^^^^^^^^^^^^^^^
#AttributeError: 'Rectangle' object has no attribute 'protctedFunc'



print ( nl, "******************************************** Print using del r1, call DTOR;" );

del r1

print (nl, "***********  END OF PROGRAM *********************************");
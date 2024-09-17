#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import SimpleDS;

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class Inheritance 2");

print ( nl, "********************************************  create derived Point, using base static Factory func: g1_p = SimpleDS.Geometry.create(1);" );

g1_p = SimpleDS.Geometry.create(1);
print ( nl," g1_p =  ", g1_p);
# NOTE: its a ref to a C++ pointer
# [PYTHON CODE] :   g1_p =   <SimpleDS.Geometry; proxy of <Swig Object of type 'Geometry *' at 0x7f613aa56e80> >

print ( nl," type(g1_p)=  ", type(g1_p) );
#[PYTHON CODE] :   type(g1_p)=   <class 'SimpleDS.Geometry'>
 
print ( nl, "******************************************** call base pure virtual func:  g1_p.draw();" );

print ( nl," g1_p.draw() =  ", g1_p.draw());

print ( nl, "******************************************** delete point using base static sunc :  SimpleDS.Geometry.destroy(g1_p);" );

SimpleDS.Geometry.destroy(g1_p);
print ( nl," g1_p =  ", g1_p);
print ( nl," type(g1_p)=  ", type(g1_p) );


print ( nl, "********************************************  g1_c = SimpleDS.Geometry.create(2);" );

g1_c = SimpleDS.Geometry.create(2);
print ( nl," g1_c =  ", g1_c);
print ( nl," type(g1_c)=  ", type(g1_c) );

print ( nl, "******************************************** only derived func:non-virtual:  g1_c.draw();" );

print ( nl," g1_c.draw() =  ", g1_c.draw());

print ( nl, "******************************************** overriden func:  SimpleDS.Geometry.destroy(g1_c);" );

#SimpleDS.Geometry.destroy(g1_c);                   its working
del g1_c;
#NOTE: deleting via 'del' , only removes the pointer, but didnot free C++ memory, becoz g1_c is holding ref to C++ ptr, instead of C++ object.

#print ( nl," g1_c =  ", g1_c);
#Traceback (most recent call last):
#  File "<>/FAST3_Python/v2/python/inheritance2.py", line 45, in <module>
#    print ( nl," g1_c =  ", g1_c);
#                            ^^^^
#NameError: name 'g1_c' is not defined. Did you mean: 'g1_p'?

#print ( nl," type(g1_c)=  ", type(g1_c) ); //same error as above



print (nl, "***********  END OF PROGRAM *********************************");
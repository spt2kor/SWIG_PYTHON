#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import copy
import STDLib;

def Print(v):
    #xi = v.begin();
    i =0;
    #print( [x for x in v]);

    while(i < v.size() ):
        print (f" index= {i} , value = {v[i]} ");
        i=i+1;
        

#==================================================================    
nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class testing String.i");

print ( nl, "******************************************** Print module  STDLib \n" );
print ( nl," STDLib =  ", STDLib);
print ( nl," type(STDLib)  =  ", type(STDLib) );
print ( nl," dir(STDLib)  =  ", dir(STDLib) );

print ( nl, "******************************************** v1 = STDLib.vectori(5) \n" );
v1 = STDLib.vectori(5);

print ( nl," v1 =  ", v1);
print ( nl," v1.size() =  ", v1.size());
print ( nl," type(v1)  =  ", type(v1) );

for i in range (0,5):
    v1[i] = i;


print ( nl, "******************************************** Print(v1); \n" );
Print(v1);

print ( nl, "******************************************** double average(std::vector<int> v); \n" );
print ( nl," STDLib.average( v1) =  ", STDLib.average( v1));


print ( nl, "******************************************** v1 = STDLib.vectord(5) \n" );
v2 = STDLib.vectord(5);

print ( nl," v2 =  ", v2);
print ( nl," v2.size() =  ", v2.size());
print ( nl," type(v2)  =  ", type(v2) );

for i in range (0,5):
    v2[i] = i + 10.0;

print ( nl, "******************************************** Print(v2); \n" );
Print(v2);

print ( nl, "******************************************** std::vector<double> half(const std::vector<double>& v) ;  \n" );
v3 = STDLib.half( v2);
#Print(v3);
#Traceback (most recent call last):
#  File "<>/FAST3_Python/v4/python/vector.py", line 64, in <module>
#    Print(v3);
#    ^^^^^^^^^
#  File "<>/FAST3_Python/v4/python/vector.py", line 16, in Print
#    while(i < v.size() ):
#              ^^^^^^
#AttributeError: 'tuple' object has no attribute 'size'

print( [x for x in v3]);
print ( nl, "******************************************** void halve_in_place(std::vector<double>& v) ; \n" );
STDLib.halve_in_place( v2);
Print(v2);

print ( nl, "******************************************** bool operator==(const std::vector<double>& v1 , const std::vector<double>& v2 ); \n" );
#print ( nl," STDLib.operator==(v2,v3) =  ", STDLib.operator==(v2,v3));
#ttributeError: module 'STDLib' has no attribute 'operator'

#swig/../cpp/vect.h:20: Warning 503: Can't wrap 'operator ==' unless renamed to a valid identifier.


print ( nl," (v2 == v3) =  ",(v2 == v3));
#//NOTE: Does not call to C++ operator==(), it does python == comparision

#print ( nl," (v2 === v3) =  ",(v2 === v3));
print ( nl, "******************************************** del v1  \n" );
del v1;

print (nl, "***********  END OF PROGRAM *********************************");
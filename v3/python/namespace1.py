
#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import copy

import Perl5ToCpp;

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class testing namespace");

print ( nl, "******************************************** Print module  Perl5ToCpp \n" );
print ( nl," Perl5ToCpp =  ", Perl5ToCpp);
print ( nl," type(Perl5ToCpp)  =  ", type(Perl5ToCpp) );
print ( nl," dir(Perl5ToCpp)  =  ", dir(Perl5ToCpp) );

print ( nl, "******************************************** global Perl5ToCpp.Math.add(2,3);" );

#print ( nl," Perl5ToCpp.Math.add(2,3) =  ", Perl5ToCpp.Math.add(2,3));
#Traceback (most recent call last):
#  File "<>/FAST3_Python/v3/python/namespace1.py", line 24, in <module>
#    print ( nl," Perl5ToCpp.Math.add(2,3) =  ", Perl5ToCpp.Math.add(2,3));
#                                                ^^^^^^^^^^^^^^^
#AttributeError: module 'Perl5ToCpp' has no attribute 'Math'

print ( nl," Perl5ToCpp.add(2,3) =  ", Perl5ToCpp.add(2,3));

print ( nl, "******************************************** r1 =  Perl5ToCpp.Math.Add();   " );
#r1 =  Perl5ToCpp.Math.Add(); 
#AttributeError: module 'Perl5ToCpp' has no attribute 'Math'

r1 =  Perl5ToCpp.Add(); 
print ( nl," r1 =  ", r1);
print ( nl," type(r1) =  ", type(r1));

print ( nl, "******************************************** r1.add(5,6);   " );
print ( nl," r1.add(5,6) =  ", r1.add(5,6));


print("----------------------")


del r1;

print (nl, "***********  END OF PROGRAM *********************************");
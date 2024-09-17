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

print ( nl, "******************************************** Print Macro SimpleDS.ADD" );

#print ( nl," SimpleDS.ADD =  ", SimpleDS.ADD , ", type( SimpleDS.ADD ) =  ", type(SimpleDS.ADD ) );
#Traceback (most recent call last):
#  File "/home/relman.ivcs/rajput/flow_arch_sandbox/FAST3_Python/v2/python/pointer1.py", line 27, in <module>
#    print ( nl," SimpleDS.ADD =  ", SimpleDS.ADD , ", type( SimpleDS.ADD ) =  ", type(SimpleDS.ADD ) );
#                                    ^^^^^^^^^^^^
#AttributeError: module 'SimpleDS' has no attribute 'ADD'


print ( nl, "******************************************** Print global variable SimpleDS.cvar.pi" );
print ( nl," SimpleDS.cvar =  ", SimpleDS.cvar);
print ( nl," type(SimpleDS.cvar)=  ", type(SimpleDS.cvar) );
print ( nl," dir (SimpleDS.cvar)=  ", dir (SimpleDS.cvar) );
print ( nl," SimpleDS.cvar.ADD =  ", SimpleDS.cvar.ADD);

print ( nl, "******************************************** SimpleDS.execute_op(20,30,SimpleDS.cvar.ADD) \n" );
print ( nl," SimpleDS.execute_op(20,30,SimpleDS.cvar.ADD)  =  ", SimpleDS.execute_op(20,30,SimpleDS.cvar.ADD) );



print ( nl, "******************************************** SimpleDS.execute_op(20,30,SimpleDS.cvar.MULTIPLY) \n" );
print ( nl," SimpleDS.execute_op(25,35,SimpleDS.cvar.MULTIPLY)  =  ", SimpleDS.execute_op(25,35,SimpleDS.cvar.MULTIPLY) );


print (nl, "***********  END OF PROGRAM *********************************");

















#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import SimpleDS;

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class Singleton");

print ( nl, "********************************************   SimpleDS.Singleton.count();" );

print ( nl," SimpleDS.Singleton.count() =  ", SimpleDS.Singleton.count() );

print ( nl, "********************************************   r1 = SimpleDS.Singleton.getInstance();" );

r1 =  SimpleDS.Singleton.getInstance() ;

print ( nl," r1 =  ", r1);
print ( nl," type(r1)=  ", type(r1) );
print ( nl," SimpleDS.Singleton.count() =  ", SimpleDS.Singleton.count() );
print ( nl, "********************************************   r1.show(); " );
r1.show();

print ( nl, "******************************************** r1.set(104,204) ; ");

r1.set(104,204) ; 
r1.show();

print ( nl, "********************************************   r2 = SimpleDS.Singleton.getInstance();" );

r2 =  SimpleDS.Singleton.getInstance() ;

print ( nl," r2 =  ", r2);
print ( nl," type(r2)=  ", type(r2) );
print ( nl," SimpleDS.Singleton.count() =  ", SimpleDS.Singleton.count() );
print ( nl, "********************************************   r2.show(); " );
r2.show();

print ( nl, "********************************************   r2 = SimpleDS.Singleton.destroyInstance();" );

SimpleDS.Singleton.destroyInstance() ;
print ( nl," SimpleDS.Singleton.count() =  ", SimpleDS.Singleton.count() );

print ( nl, "******************************************** Print using del r1, call DTOR;" );

del r1; # NOTE: not able to delete the singleton objct.

print (nl, "***********  END OF PROGRAM *********************************");

#//NOTE: singleton object gets deleted automatically by python. if we dont call destroyInstance() explicitly
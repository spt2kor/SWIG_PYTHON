#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import copy

import INHRT;

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class Inheritance 3");

print ( nl, "******************************************** Print checkig module  INHRT \n" );
print ( nl," INHRT =  ", INHRT);
print ( nl," type(INHRT)  =  ", type(INHRT) );

print ( nl," dir(INHRT)  =  ", dir(INHRT) );

print ( nl, "******************************************** creating Python class CEO(INHRT.Manager)\n" );

class CEO(INHRT.Manager):
    def __init__(self,name,age):
        INHRT.Manager.__init__(self,name);
        self.age = age;
    
    def getPosition(self):
        return f"CEO";

    def getAge(self):
        return self.age;

    def show(self):
        return f" {self.getName()} , age = {self.age} , {self.getTitle()}";

    def myType():
        return f"Python : CEO class , {type(CEO)} , derived from INHRT.Manager , its type {type(INHRT.Manager)}";

    def __del__(self):
        print(f"CEO::__del__() called for {self.getTitle()}");


print ( nl, "********************************************  r1 = CEO();" );

r1 = CEO("SAM" , 60 );

print ( nl," r1 =  ", r1);
print ( nl," type(r1)=  ", type(r1) );

print ( nl, "******************************************** : base non-virtual func:  r1.getName();" );

print ( nl," r1.getName() =  ", r1.getName());

print ( nl, "******************************************** overriden func:  r1.getPosition();" );

print ( nl," r1.getPosition() =  ", r1.getPosition());

print ( nl, "******************************************** sbase non-virtual func:: r1.getTitle();" );

print ( nl," r1.getTitle() =  ", r1.getTitle());

print ( nl, "******************************************** check ownership : r1.thisown;" );

print ( nl," r1.thisown =  ", r1.thisown ) ;

print ( nl, "******************************************** sbase non-virtual func:: r1.show();" );

print ( nl," r1.show() =  ", r1.show());

print ( nl, "******************************************** check ownership : r1.myType();" );

print ( nl," CEO.myType() =  ", CEO.myType() ) ;

print ( nl, "******************************************** r2 = copy.deepcopy(r1);" );
#r2 = copy.deepcopy(r1);
#print ( nl," r1 =  ", r1);
#print ( nl," type(r1)=  ", type(r1) );

print ( nl, "******************************************** Print using del r1, call DTOR;" );

del r1;
#NOTE: calls CEO DTOR first, and interanlly calls C++ Employee DTOR automatically.
#[PYTHON CODE] :  ******************************************** Print using del r1, call DTOR;
#CEO::__del__() called
#~Employee() @ 0x5654180a03e0

print ( nl, "********************************************  r3 = CEO(\"JOHN\",50);" );

r3 = CEO("JOHN" , 50 );


#r3.thisown = False; // NO effect of this

print ( nl," r3.thisown =  ", r3.thisown ) ;

r3 = r3.__disown__();

print ( nl," r3.thisown =  ", r3.thisown ) ;

print ( nl, "********************************************  list = INHRT.EmployeeList();" );

list = INHRT.EmployeeList();

print ( nl, "********************************************  list.addEmployee(r3);" );

list.addEmployee(r3);

print ( nl, "********************************************  print the employee list " );
print("(position, title) for items 0-3:")

print("  %s, \"%s\"" % (list.get_item(0).getPosition(), list.get_item(0).getTitle()))
print("  %s, \"%s\"" % (list.get_item(1).getPosition(), list.get_item(1).getTitle()))
print("  %s, \"%s\"" % (list.get_item(2).getPosition(), list.get_item(2).getTitle()))
print("  %s, \"%s\"" % (list.get_item(3).getPosition(), list.get_item(3).getTitle()))

print("----------------------")

del list;
print("----------------------")

#r3.disown();
#AttributeError: 'CEO' object has no attribute 'disown'. Did you mean: 'thisown'?


print (nl, "***********  END OF PROGRAM *********************************");
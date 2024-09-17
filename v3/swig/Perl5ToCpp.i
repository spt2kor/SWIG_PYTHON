/*my module name*/
%module Perl5ToCpp
//=======================================
%{
    #include "Callback.h"
    //#include "std_lib.h"
    //#include "pointers1.h"
%}
//=======================================

/* turn on director wrapping Callback */
%feature("director") Callback;

/* Caller::setCallback(Callback *cb) gives ownership of the cb to the
 * Caller object.  The wrapper code should understand this. */
%apply SWIGTYPE *DISOWN { Callback *cb };

//=======================================
//file:///C:/src/swigwin-4.1.1/Examples/perl5/pointer/example.i
/* This example illustrates a couple of different techniques
   for manipulating C pointers */
/* First we'll use the pointer library */
//extern void add(int *x, int *y, int *result);

%include cpointer.i
%pointer_functions(int, intp);
%pointer_functions(double, double_p);

//=======================================
/* Next we'll use some typemaps */
%include typemaps.i
//extern void subtract(int *INPUT, int *INPUT, int *OUTPUT);
//=======================================
/* Next we'll use typemaps and the %apply directive */
%apply int *OUTPUT { int *r };
//extern int divide(int n, int d, int *r);

//=======================================
//%include "carrays.i"
//%array_functions(int, IntTransformer);

//void Transform(int x[3]);

//=======================================
%include "../cpp/Callback.h"
//%include "../cpp/pointers1.h"
//%include "../cpp/std_lib.h"
//=======================================
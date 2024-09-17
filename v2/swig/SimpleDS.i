/*my module name*/
%module SimpleDS

/*my functions list - goes to generated cpp wrapper files.*/
%{
#include "Singleton.h"
#include "Shape.h"
#include "SimpleDS.h"
#include "DataTypes.h"
#include "Pointer.h"
//#include "Pointer1.h" // Undefined subroutine &SimpleDS::divide called at perl/Pointer1.pl line 19.

//NOTE: if we miss to add the .h file here, 
//ERROR: AttributeError: module 'SimpleDS' has no attribute 'Geometry'

%}


/* list of exported functions*/
/*#include "SimpleDS.h" not working*/

%include "../cpp/Singleton.h"
%include "../cpp/Shape.h"
%include "../cpp/SimpleDS.h"
%include "../cpp/DataTypes.h"
%include "../cpp/Pointer.h"
//%include "../cpp/Pointer1.h"

//NOTE: if we miss to add the .h file here, 
//ERROR: AttributeError: module 'SimpleDS' has no attribute 'Geometry'


//%constant (int (*)(int,int)) ADDI = addition;// BOT REQUIRED, works Directly with FUNCPTR

//%implicit(A, int, double, B); //NOTE: Pending test type conversion

/*
extern double pi;
#define RED 0xFF0000
#define VERSION 1
extern int calculateArea(int width, int height);

*/

/*
list of C++/SWIG warnings and depricated feature list
http://web.mit.edu/ghudson/trac/src/swig-1.3.25/Doc/Manual/Warnings.html
https://www.swig.org/Doc1.3/Warnings.html

*/

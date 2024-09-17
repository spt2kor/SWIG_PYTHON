%module(directors="1") INHRT
%{
#include "inheritance1.h"
%}

%include "std_vector.i"
%include "std_string.i"

/* turn on director wrapping for Manager */
%feature("director") Employee;
%feature("director") Manager;

/* EmployeeList::addEmployee(Employee *p) gives ownership of the
 * employee to the EmployeeList object.  The wrapper code should
 * understand this. */
%apply SWIGTYPE *DISOWN { Employee *p };

%include "../cpp/inheritance1.h"



//https://www.swig.org/Doc4.0/SWIGPlus.html#SWIGPlus_target_language_callbacks
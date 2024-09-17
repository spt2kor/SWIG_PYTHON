/*my module name*/
%module SimpleDS

/*my functions list - goes to generated cpp wrapper files.*/
%{
    #include "SimpleDS.h"

%}

%include "../cpp/SimpleDS.h"







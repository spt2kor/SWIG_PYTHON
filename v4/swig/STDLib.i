/*my module name*/
%module STDLib
//=======================================
%{
    #include "str.h"
    
    #include "vect.h"
    #include "map.h"
    //#include "umap.h"
%}


//=======================================
%include "std_string.i"

%apply const std::string& {std::string* }; //required for changePerlStrPtr()

%apply const std::string& {std::string& };// Not working

%include "../cpp/str.h"
//=======================================

%include "std_vector.i"

namespace std {
    %template(vectori) vector<int>;
    %template(vectord) vector<double>;
};

%include "../cpp/vect.h" 
//=======================================
/*
%include "std_unordered_map.i"

namespace std {
    %template(unordered_map_ii) unordered_map<int,int>;
    %template(unordered_map_sd) unordered_map<string,double>;
};

%include "../cpp/umap.h"

// rajput@vihlc1771[FAST2/v4]{master} make map
// swig -c++ -perl -outdir generated_files -o generated_files/STDLib_wrap.cpp swig/STDLib.i
// swig/STDLib.i:31: Error: Unable to find 'std_unordered_map.i'
// make: *** [generated_files/STDLib_wrap.cpp] Error 1

*/


//=======================================

%include "std_map.i"

namespace std {
    %template(map_ii) map<int,int>;
    %template(map_sd) map<string,double>;
};

%include "../cpp/map.h"

//=======================================

//=======================================

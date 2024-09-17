//===========================================================================
#include "vect.h"
#include "Log.h"
#include <algorithm>
#include <numeric>                  //std::accumulate()

//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "[VECTOR]"
//===========================================================================


//===========================================================================
double average(std::vector<int> v) {
    FUNC_START;

    auto res = std::accumulate(v.begin(), v.end(), 0.0)/v.size(); //numeric
    FUNC_END;
    return res;
}

std::vector<double> half(const std::vector<double>& v) {
    FUNC_START;

    std::vector<double> w(v);
    for (unsigned int i=0; i<w.size(); i++)
        w[i] /= 2.0;

    FUNC_END;
    return w;
}

void halve_in_place(std::vector<double>& v) {
    FUNC_START;

    for (std::vector<double>::iterator it = v.begin(); it != v.end(); ++it)
        *it /= 2.0;

    FUNC_END;
}


//===========================================================================


bool operator==(const std::vector<double>& v1 , const std::vector<double>& v2 )
{
    FUNC_START;
    if(v1.size() != v2.size()){
        CPP_CODE_MSG(" : size is diff ");
        return false;
    }

    for (int i=0;i<v1.size();++i)
        if(v1[i] != v2[i]){
            CPP_CODE_MSG(" : alue is different at i = ");
            PRINT_VAR(i);
            return false;
        }

    FUNC_END; 
    return true;

}

//===========================================================================


//===========================================================================










//===========================================================================

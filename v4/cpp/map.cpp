//===========================================================================
#include "map.h"
#include "Log.h"
#include <algorithm>
#include <numeric>                  //std::accumulate()

//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "[MAP]"
//===========================================================================

#define PRINT_KV_VAR(x,y) {CPP_CODE_MSG;cout<<", " #x " = "<< ( x )<<", " #y " = "<< ( y )<<endl;}


int printMapII(map<int,int> mp)
{
    FUNC_START;


    auto print_key_value = [](const auto& key, const auto& value)
    {
        PRINT_KV_VAR(key,value);
        
        //std::cout << "Key:[" << key << "] Value:[" << value << "]\n";
    };

    for (const auto& n : mp)
        print_key_value(n.first, n.second);

    FUNC_END;
    return mp.size();
}


//===========================================================================
int printMapSD(map<string,double> mp)
{
    FUNC_START;
    auto print_key_value = [](const auto& key, const auto& value)
    {
        PRINT_KV_VAR(key,value);
        //std::cout << "Key:[" << key << "] Value:[" << value << "]\n";
    };

    for (const auto& n : mp)
        print_key_value(n.first, n.second);

    FUNC_END;
    return mp.size();
}

//===========================================================================

map<string,double> PrintMapCR(const map<string,double> & mp) 
{
    FUNC_START;
    auto print_key_value = [](const auto& key, const auto& value)
    {
        PRINT_KV_VAR(key,value);
        //std::cout << "Key:[" << key << "] Value:[" << value << "]\n";
    };

    for (const auto& n : mp)
        print_key_value(n.first, n.second);

    auto mp1 (mp);

    FUNC_END;
    return mp1;
}


//===========================================================================









//===========================================================================

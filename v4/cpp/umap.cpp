//===========================================================================
#include "umap.h"
#include "Log.h"
#include <algorithm>
#include <numeric>                  //std::accumulate()

//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "[UNORDERED_MAP]"
//===========================================================================




int printMapII(unordered_map<int,int> mp)
{
    FUNC_START;


    auto print_key_value = [](const auto& key, const auto& value)
    {
        PRINT_VAR(key);
        PRINT_VAR(value);
        //std::cout << "Key:[" << key << "] Value:[" << value << "]\n";
    };

    for (const auto& n : mp)
        print_key_value(n.first, n.second);

    FUNC_END;
    return mp.size();
}


//===========================================================================
int printMapSD(unordered_map<string,double> mp)
{
    FUNC_START;
    auto print_key_value = [](const auto& key, const auto& value)
    {
        PRINT_VAR(key);
        PRINT_VAR(value);
        //std::cout << "Key:[" << key << "] Value:[" << value << "]\n";
    };

    for (const auto& n : mp)
        print_key_value(n.first, n.second);

    FUNC_END;
    return mp.size();
}

//===========================================================================

unordered_map<string,double> PrintMapCR(const unordered_map<string,double> & mp) 
{
    FUNC_START;
    auto print_key_value = [](const auto& key, const auto& value)
    {
        PRINT_VAR(key);
        PRINT_VAR(value);
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

//===========================================================================
#include "str.h"
#include "Log.h"
//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "[STR]"
//===========================================================================



string moduleName = "STDLib";
//const string fileName = "str.h";
//===========================================================================
void PrintStr(string perltxt )
{
    FUNC_START;
    PRINT_VAR(perltxt);
    FUNC_END;
}


string UpdateStr(const string& perltxt )
{
    FUNC_START;
    PRINT_VAR(perltxt);
    string cpptxt = "{C++ received the $" + perltxt + "}";

    PRINT_VAR(cpptxt);
    FUNC_END;
    return cpptxt;
}

string changePerlStr(string& perltxt )
{
    FUNC_START;
    PRINT_VAR(perltxt);
    perltxt = "{C++ received the $" + perltxt + "}";
    FUNC_END;
    return perltxt;
}

string* changePerlStrPtr(string* perltxt )
{
    FUNC_START;
    string& perlstrRef = *perltxt;
    PRINT_VAR(perlstrRef);
    perlstrRef = "{C++ received the $" + perlstrRef + "}";

    //perltxt[3] = '#';  //ERROR causing segmentation fault
    FUNC_END;
    return &perlstrRef;
}
//===========================================================================


const string StrTest::m_fileName = "str.cpp";


StrTest::StrTest():m_perltxt("Default StrTest String"){
    CLASS_FUNC_START;
    PRINT_VAR(m_perltxt);
    CLASS_FUNC_END;
}


StrTest::~StrTest() {
    CLASS_FUNC_START;
    PRINT_VAR(m_perltxt);
    CLASS_FUNC_END;
}

string StrTest::UpdateStr(const string& perltxt )
{
    CLASS_FUNC_START;
    PRINT_VAR(perltxt);
    m_perltxt = perltxt;

    string cpptxt = "  [C++ received the #" + perltxt + " ] ";

    PRINT_VAR(cpptxt);
    CLASS_FUNC_END;
    return cpptxt;
}

//===================================================

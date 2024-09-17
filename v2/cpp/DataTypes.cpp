// #include <iostream>
// #include <string>
// #include <string.h>
// #include <typeinfo>
#include "DataTypes.h"

// using namespace std;

static Algo a2(999);

Algo *pA1 = &a2;
const char *foo = "Hello World\n";//try setting this value?
//=========================================================================
#define CPP_CODE_MSG ("\n[C++ Code], Algo::")
#define FUNC_START {cout<<CPP_CODE_MSG<<__FUNCTION__<<"() started.["<<(void*)(this)<<"]"<<endl;}
#define FUNC_END {cout<<CPP_CODE_MSG<<__FUNCTION__<<"() exited."<<endl;}
#define PRINT {cout<<CPP_CODE_MSG<<__FUNCTION__<<"(), pub = "<<pub<<endl;}

//=========================================================================
Algo::Algo(int pub):pub(pub)
{
    FUNC_START;
    PRINT;
    FUNC_END;
}

Algo::~Algo()
{
    FUNC_START;
    PRINT;
    FUNC_END;
}

Algo::Algo(const Algo &o) 
{
    FUNC_START;
    pri = o.pri;
    pub = o.pub;
    FUNC_END;
}

Algo& Algo::operator=(const Algo &o){
    FUNC_START;
    pub = o.pub;
    FUNC_END;
    return *this;
}
//============================================================

void Algo::print()
{
    FUNC_START;
    PRINT;
    FUNC_END;
}


Algo* Algo::clone()
{
    FUNC_START;
    Algo* r1 = new Algo(*this);
    FUNC_END;
    return r1;
}

bool Algo::classInfo()
{
    //FUNC_START;
    {cout<<CPP_CODE_MSG<<__FUNCTION__<<"() started."<<endl;}
    cout<<CPP_CODE_MSG<<"class details: "<<typeid(Algo).name()<< endl;
    FUNC_END;
    return true;
}

//=========================================================================


//
// Factory method for all the Geometry objects
//
Geometry* Geometry::create(int type) {
    switch (type) {			     
    case 1: return new Point();	     
    case 2: return new Circle(); 	     
    default: return 0;			     
    }					     
}	

void Geometry::destroy(Geometry* p)
{        
    {cout<<CPP_CODE_MSG_G<<__PRETTY_FUNCTION__<<", started.["<<(void*)(p)<<"]"<<endl;}
    delete p;
    FUNC_END_G;
}

//=========================================================================
int getAii(A a) { 
    return a.ii; 
}



//=========================================================================


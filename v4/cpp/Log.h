#pragma once
#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <typeinfo>

using namespace std;

//=========================================================================
#define CLASS_NAME ""
#define CPP_CODE_MSG {cout<<"\n[C++ Code], "<<CLASS_NAME<<"::"<<__FUNCTION__<<"(), ";}

#define CLASS_FUNC_START_STATIC {CPP_CODE_MSG;cout<<"started."<<endl;}

#define CLASS_FUNC_START {CPP_CODE_MSG;cout<<"started.["<<(void*)(this)<<"]"<<endl;}
#define CLASS_FUNC_END {CPP_CODE_MSG;cout<<"exited."<<endl;}

#define FUNC_START {CPP_CODE_MSG;cout<<"started."<<endl;}
#define FUNC_END {CPP_CODE_MSG;cout<<" exited."<<endl;}

#define PRINT_VAR(x) {CPP_CODE_MSG;cout<<", " #x " = "<< ( x )<<endl;}


//=========================================================================
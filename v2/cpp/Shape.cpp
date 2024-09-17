#include <iostream>
#include <string>
#include <string.h>
#include <typeinfo>
#include "Shape.h"

using namespace std;


//=========================================================================
#define CPP_CODE_MSG ("\n[C++ Code], Shape::")
#define FUNC_START {cout<<CPP_CODE_MSG<<__FUNCTION__<<"() started.["<<(void*)(this)<<"]"<<endl;}
#define FUNC_END {cout<<CPP_CODE_MSG<<__FUNCTION__<<"() exited."<<endl;}

#define SHOW_NAME {                 \
    if(name)                        \
        cout<<CPP_CODE_MSG<<__FUNCTION__<<"(), Shape's name =["<<(name)<<"]"<<endl;       \
    }                               \
    ;



//=========================================================================
Shape::Shape(char* ptr):name(nullptr)
{
    {cout<<CPP_CODE_MSG<<"Shape(char* ptr)() started.["<<(void*)(this)<<"]"<<endl;}
    setName(ptr);
    //SHOW_NAME;
    FUNC_END;
}

Shape::~Shape()
{
    {cout<<CPP_CODE_MSG<<"~Shape() started.["<<(void*)(this)<<"]"<<endl;}
    SHOW_NAME;
    FUNC_END;
}

Shape::Shape(const Shape &o) : name(nullptr)
{
    {cout<<CPP_CODE_MSG<<"Shape(const Shape &o) started.["<<(void*)(this)<<"]"<<endl;}
    setName(o.name);
    SHOW_NAME;
    FUNC_END;
}
Shape& Shape::operator=(const Shape &o){
    {cout<<CPP_CODE_MSG<<"operator=(const Shape &o) started.["<<(void*)(this)<<"]"<<endl;}
    setName(o.name);
    SHOW_NAME;
    FUNC_END;
    return *this;
}
//============================================================

void Shape::privateFunc(){
    FUNC_START;
    SHOW_NAME;
    FUNC_END;
}

void Shape::protctedFunc(){
    FUNC_START;
    SHOW_NAME;    
    FUNC_END;
}

void Shape::show()
{
    FUNC_START;
    SHOW_NAME;    
    FUNC_END;
}

char* Shape::getName()
{
    FUNC_START;
    SHOW_NAME;    
    FUNC_END;
    return name;
}

// Shape Shape::clone()
// {
//     FUNC_START;
//     Rectangle r1(height,width);
//     FUNC_END;
//     return r1;
// }
void Shape::setName(const char* ptr)
{
    FUNC_START;
    if(ptr)
    {
        auto len = strlen(ptr);
        if(name)
            delete[] name;
        name = nullptr;
        cout<<CPP_CODE_MSG<<" input name = {"<<ptr<<"}, (void*)(ptr) = "<<(void*)(ptr) <<endl;
        
        name = new char[len+1];
        memcpy(name,ptr,len);
        name[len]='\0';
        cout<<CPP_CODE_MSG<<" new setName is = "<<name <<", (void*)(name) = "<<(void*)(name)<<endl; 
    }
    else
    {
        cout<<CPP_CODE_MSG<<" char* is NULL  "<<endl;
    }
    FUNC_END;
}

void Shape::copy(const Shape &src)
{
    FUNC_START;
    setName(src.name);
    FUNC_END;
}

bool Shape::classInfo()
{
    //FUNC_START;
    {cout<<CPP_CODE_MSG<<__FUNCTION__<<"() started."<<endl;}
    cout<<CPP_CODE_MSG<<"class details: "<<typeid(Shape).name()<< endl;
    FUNC_END;
    return true;
}

//=========================================================================
#include <iostream>
#include <typeinfo>
#include "SimpleDS.h"
#include "Log.h"

using namespace std;


//=========================================================================
double pi = 3.14;

const char* const class_name = "custome class SimpleDS::Rectangle"; 

//===========================================
//char* class_name = "custome class SimpleDS::Rectangle";    NOTE : compiler error
/*g++ -std=c++11 -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/SimpleDS.cpp -o generated_files/obj/SimpleDS.o
cpp/SimpleDS.cpp:11:20: warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]
   11 | char* class_name = "custome class SimpleDS::Rectangle";
      |                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
//===========================================


int some_no = 1001;
#undef  CLASS_NAME
#define CLASS_NAME "[SimpleDS]"



//=========================================================================
Rectangle::~Rectangle() 
{
    CLASS_FUNC_START;

    CLASS_FUNC_END;
}

Rectangle::Rectangle(int height, int width) : height(height), width(width)
{
    CLASS_FUNC_START;

    CLASS_FUNC_END;
}

Rectangle::Rectangle(const Rectangle &o) : height(o.height), width(o.width)
{
    CLASS_FUNC_START;
    
    CLASS_FUNC_MSG("Rectangle::Rectangle(const Rectangle &o)");
    
    CLASS_FUNC_END;
}

Rectangle &Rectangle::operator=(const Rectangle &o)
{
    CLASS_FUNC_START;
    
    height = o.height;
    width = o.width;

    CLASS_FUNC_END;
    return *this;
}


bool Rectangle::set(int h, int w)
{
    CLASS_FUNC_START;
    
    height = h;
    width = w;

    CLASS_FUNC_END;
    return true;
}

int Rectangle::area(){
    CLASS_FUNC_START;
    auto area = width * height;
    CLASS_FUNC_END;
    return area;
}

void Rectangle::show()
{
    CLASS_FUNC_START;
    cout << endl<< "Rectangle details: height : "<<height<<", width : "<<width << endl;
    CLASS_FUNC_END;
}

Rectangle Rectangle::clone()
{
    CLASS_FUNC_START;
    Rectangle r1(height,width);
    CLASS_FUNC_END;
    return r1;
}

bool Rectangle::classInfo()
{
    CLASS_FUNC_START_STATIC;
    cout << endl<< "class details: "<<typeid(Rectangle).name()<< endl;
    CLASS_FUNC_END;
    return true;
}

//=========================================================================
int calculateArea(int width, int height)
{
        FUNC_START;
        auto area = width * height;
        cout<<"\n value of pi = "<<pi <<", and color REd = "<<RED<<endl;
        FUNC_END;
        return area;
}

//=========================================================================
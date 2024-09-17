#include <iostream>
#include <string>
#include <string.h>
#include <typeinfo>
#include "SimpleDS.h"

using namespace std;

//=========================================================================
double pi = 3.14;
int arr[5] = {2, 4, 6, 8, 10};

int some_no = 1001;
const char* const class_name = "custome class SimpleDS::Rectangle"; 


#define CPP_CODE_MSG ("\n[C++ Code], Rectangle::")
#define FUNC_START                                                                               \
    {                                                                                            \
        cout << CPP_CODE_MSG << __FUNCTION__ << "() started.[" << (void *)(this) << "]" << endl; \
    }

#define FUNC_END                                                      \
    {                                                                 \
        cout << CPP_CODE_MSG << __FUNCTION__ << "() exited." << endl; \
    }

//=========================================================================
Rectangle::Rectangle(char *name, int height, int width) : Shape(name), height(height), width(width)
{
    FUNC_START;
    if (!name)
        setName("Default-Rect");
    FUNC_END;
}

Rectangle::Rectangle(int height, int width) : Shape("Default-Rect"), height(height), width(width)
{
    FUNC_START;

    FUNC_END;
}

Rectangle::~Rectangle()
{
    FUNC_START;
    // NOTE: check do we need to call the Shape::DTOR
    FUNC_END;
}

Rectangle::Rectangle(const Rectangle &o) : Shape(o), height(o.height), width(o.width)
{
    FUNC_START;

    FUNC_END;
}

Rectangle &Rectangle::operator=(const Rectangle &o)
{
    FUNC_START;

    Shape::operator=(o);
    height = o.height;
    width = o.width;

    FUNC_END;
    return *this;
}
//============================================================

void Rectangle::privateFunc()
{
    FUNC_START;

    FUNC_END;
}

void Rectangle::protctedFunc()
{
    FUNC_START;
    FUNC_END;
}

int Rectangle::area()
{
    FUNC_START;
    auto area = width * height;
    FUNC_END;
    return area;
}

void Rectangle::show()
{
    FUNC_START;
    Shape::show();
    cout << CPP_CODE_MSG << "show(), Rectangle details: height : " << height << ", width : " << width << endl;
    FUNC_END;
}

Rectangle Rectangle::clone()
{
    FUNC_START;
    Rectangle r1(*this);
    FUNC_END;
    return r1;
}

Rectangle &Rectangle::returnSelfRef()
{
    FUNC_START;
    FUNC_END;
    return *this;
}

Rectangle *Rectangle::returnSelfPtr()
{
    FUNC_START;
    FUNC_END;
    return this;
}

void Rectangle::copy(const Rectangle &src)
{
    FUNC_START;

    Shape::copy(src);
    height = src.height;
    width = src.width;

    FUNC_END;
}

bool Rectangle::classInfo()
{
    // FUNC_START;
    {
        cout << CPP_CODE_MSG << __FUNCTION__ << "() started." << endl;
    }
    Shape::classInfo();
    cout << CPP_CODE_MSG << "class details: " << typeid(Rectangle).name() << endl;
    FUNC_END;
    return true;
}


void Rectangle::set(char *name, int height, int width)
{
    FUNC_START;

    setName(name);
    this->height = height;
    this->width = width;

    FUNC_END;
}


//=========================================================================
int calculateArea(int width, int height)
{
    // FUNC_START;
    {
        cout << CPP_CODE_MSG << __FUNCTION__ << "() started." << endl;
    }
    auto area = width * height;
    cout << CPP_CODE_MSG << " value of pi = " << pi << ", and color REd = " << RED << endl;
    FUNC_END;
    return area;
}

//=========================================================================
char *passCharPtr(char *ptr)
{
    // FUNC_START;
    {
        cout << CPP_CODE_MSG << __FUNCTION__ << "() started." << endl;
    }

    auto len = strlen(ptr);
    char *nptr = ptr;
    if (ptr && len > 0)
    {
        // testing can we modify input char*=> yes we can modify and its working
        // ptr[2] = '#';
        // return ptr;

        cout << CPP_CODE_MSG << " char* ptr = " << ptr << ", (void*)(ptr) = " << (void *)(ptr) << endl;
        string str(ptr);
        cout << CPP_CODE_MSG << " str  = " << str << endl;

        const char *ptr1 = "{this is C++ string}";
        len = strlen(ptr1);
        nptr = new char[len + 1];
        memcpy(nptr, ptr1, len);
        nptr[len] = '\0';
        cout << CPP_CODE_MSG << " char* nptr = " << nptr << ", (void*)(nptr) = " << (void *)(nptr) << endl;
    }
    else
    {
        cout << CPP_CODE_MSG << " char* is NULL  " << endl;
    }

    FUNC_END;
    return nptr;
}

//=========================================================================
Rectangle *createRectangle(char *name, int w, int h)
{
    // FUNC_START;
    {
        cout << CPP_CODE_MSG << __FUNCTION__ << "() started." << endl;
    }

    Rectangle *r = new Rectangle(name, w, h);

    FUNC_END;
    return r;
}
//=========================================================================
int Accumulate(int data[]) // paasing array
{
    int sum = 0;
    for (int i = 0; i < 5; ++i)
        sum += data[i];
    return sum;
}

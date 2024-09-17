#pragma once
#include "Shape.h"
/*https://www.swig.org/Doc4.1/SWIGDocumentation.html#Introduction_nn2*/
//------------------------------------------------------------
extern double pi;

#define RED 0xFF0000

#define VERSION 1

// int arr[] = {2,4,6,8,10}; //swig/../cpp/SimpleDS.h:11: Warning 462: Unable to set dimensionless array variable
extern int arr[5]; // unable to use this array

//------------------------------------------------------------
//------------------------------------------------------------
class Rectangle : public Shape
{
private:
    int height;
    int width;
    void privateFunc(); // Can't locate object method "privateFunc" via package "SimpleDS::Rectangle" at perl/class.pl line 88.

protected:
    void protctedFunc(); // Can't locate object method "protctedFunc" via package "SimpleDS::Rectangle" at perl/class.pl line 92.

public:
    Rectangle(int height, int width);
    Rectangle(char *name = nullptr, int height = 1, int width = 1);
    ~Rectangle();
    Rectangle(const Rectangle &other); // create a new object from existing other object

    Rectangle &operator=(const Rectangle &other); // NOTE:  does not work from perl //swig/../cpp/SimpleDS.h:30: Warning 362: operator= ignored
    Rectangle clone();                            // return a new object ,but it create multiple copies internally
    void copy(const Rectangle &src);              // copy from src to this object. both objects are already created

    int area();
    void set(char *name = nullptr, int height = 1, int width = 1);
    void show();

    static bool classInfo(); // for singleton class

    Rectangle &returnSelfRef(); // works
    Rectangle *returnSelfPtr(); // works
};

// extern
int calculateArea(int width, int height);

char *passCharPtr(char *ptr); // its working we can pass perl & c++ string, back and forth.
// string  passCharPtr(string str);

Rectangle *createRectangle(char *name = nullptr, int w = 1, int h = 1); // stores the pointer in hash.;
// #NOTE
// # by default at the end of perl code, perl objects/ref deleted, they delete there c++ counterpart objects(only)
// #perl object who holds C++ ref/ptr, dont trigger DTOR
// #so if c++ code return ptr/ref, he has to take care of deletion

int Accumulate(int data[]); // paasing array


extern int some_no;


extern const char* const class_name;   

#pragma once

/*https://www.swig.org/Doc4.1/SWIGDocumentation.html#Introduction_nn2*/
class Rectangle{
    
    int height;
    int width;

public:

    Rectangle(int height, int width);
    ~Rectangle() ;
    Rectangle(const Rectangle& other);
    Rectangle& operator= (const Rectangle &other);

    int area();
    void show();
    bool set(int height, int width);
    
    Rectangle clone();
    static bool classInfo();
};

int calculateArea(int width, int height);

extern double pi;

//===========================================
//extern char* class_name;   NOTE : compiler error
/*g++ -std=c++11 -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/SimpleDS.cpp -o generated_files/obj/SimpleDS.o
cpp/SimpleDS.cpp:11:20: warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]
   11 | char* class_name = "custome class SimpleDS::Rectangle";
      |                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
//===========================================
extern const char* const class_name;   


extern int some_no;

#define RED 0xFF0000


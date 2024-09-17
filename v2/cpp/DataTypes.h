#pragma once
//------------------------------------------------------------
#include <iostream>
#include <string>
#include <string.h>
#include <typeinfo>

using namespace std;

//------------------------------------------------------------
struct Algo{

private:
    int pri = 100;

protected:
    int pro = 200;

public:
    int pub = 300;

    int getPri() {return pri;}
    int getPro() {return pro;}
    int getPub() {return pub;}

    Algo(int pub = 500);

    virtual ~Algo();
    Algo(const Algo& src);
    
    Algo& operator= (const Algo &other);//NOTE:  does not work from perl 

    //https://www.swig.org/Doc4.1/SWIGDocumentation.html#SWIG_nn22
    Algo* clone(); // NOTE: how to delete from clint code, otherwise it leaks memory
    virtual void print();
    static bool classInfo();// for singleton class
};

//https://www.swig.org/Doc4.1/SWIGDocumentation.html#SWIG_nn22
//Again some caution is in order. A global variable created in this manner will show up as a pointer in the target scripting language. It would be an extremely bad idea to free or destroy such a pointer. Also, C++ classes must supply a properly defined copy constructor in order for assignment to work correctly.
//Algo A1; //NOTE:  how to handle globle class variables? test?

extern Algo *pA1; //allocate value from client side?

extern const char *foo ;//try setting this value?

//------------------------------------------------------------
//C:\src\swigwin-4.1.1\Lib\typemaps\factory.swg
 //----  geometry.h --------
#define CPP_CODE_MSG_G ("\n[C++ Code], ")
#define FUNC_START_G {cout<<CPP_CODE_MSG_G<<__PRETTY_FUNCTION__<<"() started.["<<(void*)(this)<<"]"<<endl;}
#define FUNC_END_G {cout<<CPP_CODE_MSG_G<<__PRETTY_FUNCTION__<<"() exited."<<endl;}

struct Geometry 
{                          
    enum GeomType
    {			     
        POINT,				     
        CIRCLE				     
    };					     
                       
    virtual ~Geometry() 
    {
        FUNC_START_G;
        FUNC_END_G;
    }    		     
    virtual int draw() = 0;
//
// Factory method for all the Geometry objects
//
    static Geometry* create(int i);     
    static void destroy(Geometry* p);
};					     
                        
struct Point : Geometry  {		     
    int draw() {
        FUNC_START_G;
        FUNC_END_G;
        return 1; 
    }		     
    double width() { 
        FUNC_START_G;
        FUNC_END_G;
        return 1.0; 
    }  
    virtual ~Point() 
    {
        FUNC_START_G;
        FUNC_END_G;
    } 

};					     
                        
struct Circle : Geometry  {		     
    int draw() { 
        FUNC_START_G;
        FUNC_END_G;
        return 2; 
    }		     
    double radius() { 
        FUNC_START_G;
        FUNC_END_G;
        return 1.5;
    }  
    virtual ~Circle() 
    {
        FUNC_START_G;
        FUNC_END_G;
    }         
}; 					     

				    
//----  geometry.h --------
//======================================================================================

//C:\src\swigwin-4.1.1\Lib\typemaps\implicit.swg

    struct B { 
        int i = 100;    
    };  
    struct A
    {
      int ii;
      A(int i) { ii = 1; }
      A(double d) { ii = 2; }
      A(const B& b) { ii = 3; }
    };
  
    int getAii(A a);

    //getAii(10); => getAii (   A(10)  ) ;//not working in PERL



//======================================================================================
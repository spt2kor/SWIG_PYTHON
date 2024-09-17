#pragma once
#include <iostream>
#include <string>
#include <string.h>
#include <typeinfo>
#include <mutex>    //once_flag,call_once()
#include <memory>   //unique_ptr<>

using namespace std;
//------------------------------------------------------------
//------------------------------------------------------------

class Singleton 
{
    int height= 20;
    int width= 20;
    static uint m_count;
    static unique_ptr<Singleton> m_instance;
private:
    Singleton();
    

protected:
    
public:
    ~Singleton();
    Singleton(const Singleton& other) = delete;//create a new object from existing other object 
    Singleton& operator= (const Singleton &other)  = delete;//NOTE:  does not work from perl //swig/../cpp/SimpleDS.h:30: Warning 362: operator= ignored


    void set(  int height=0, int width=0);
    void show();

    static Singleton& getInstance();
    static void destroyInstance();
    static int count();
};



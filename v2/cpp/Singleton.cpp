//https://stackoverflow.com/questions/55490024/stdcall-once-when-should-it-be-used

#include "Singleton.h"
#include "Log.h"

#undef CLASS_NAME
#define CLASS_NAME "Singleton"

//=========================================================================
unique_ptr<Singleton> Singleton::m_instance{nullptr};
uint Singleton::m_count = {0};
//=========================================================================
Singleton::Singleton()
{
    CLASS_FUNC_START;

    CLASS_FUNC_END;
}

Singleton::~Singleton()
{
    CLASS_FUNC_START;
    //NOTE: check do we need to call the Shape::DTOR
    CLASS_FUNC_END;
}


//============================================================

void Singleton::show()
{
    CLASS_FUNC_START;
    PRINT_VAR(height);
    PRINT_VAR(width);
    CLASS_FUNC_END;
}

void Singleton::set(  int h, int w)
{
    CLASS_FUNC_START;
    height = h;
    width = w;
    PRINT_VAR(height);
    PRINT_VAR(width);
    CLASS_FUNC_END;
}

Singleton& Singleton::getInstance()
{
    CLASS_FUNC_START_STATIC;
    static once_flag flag;
    call_once(flag, [&](){m_instance.reset(new Singleton()); });

    //cout<<"started.["<<(void*)(this)<<"]"<<endl;}
    CLASS_FUNC_END;
    ++m_count;
    return *m_instance.get();
}

void Singleton::destroyInstance()
{
    CLASS_FUNC_START_STATIC;
    // static once_flag flag1;
    // call_once ( flag1 , [&]() {  
    //     auto ptr = m_instance.get(); 
    //     m_instance.reset(nullptr); 
    //     delete ptr;
    //  });
    //PRINT_VAR(height);
    //PRINT_VAR(width);
    m_count = 0;
    m_instance = nullptr; 
    CLASS_FUNC_END;
}

int Singleton::count()
{
    CLASS_FUNC_START_STATIC;
    PRINT_VAR(m_count);
    CLASS_FUNC_END;
    return m_count;
}



















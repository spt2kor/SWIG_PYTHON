//===========================================================================
#include "Callback.h"
#include "Log.h"
//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "namespace Math::"
//===========================================================================
int Math::add(int x, int y)
{
    FUNC_START;
    auto sum = x+y;
    FUNC_END;
    return sum;
}

int Math::Add::add(int x,int y)
{
    FUNC_START;
    m_x = x;
    m_y = y;
    m_sum = m_x + m_y;
    FUNC_END;
    return m_sum;
}
//===========================================================================
//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "Callback"
//===========================================================================
Callback::~Callback()
{ 
    CLASS_FUNC_START;
    CLASS_FUNC_END;
}
void Callback::run() 
{
    CLASS_FUNC_START;
    CLASS_FUNC_END;
}
Callback::Callback()
{
    CLASS_FUNC_START;
    CLASS_FUNC_END;
}
void Callback::baseName()
{
    CLASS_FUNC_START;
    CLASS_FUNC_END;
}
//===========================================================================
//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "Caller"
//===========================================================================
//===========================================================================

Caller::Caller(): _callback(0) 
{
    CLASS_FUNC_START;
    CLASS_FUNC_END;
}

Caller::~Caller() 
{ 
    CLASS_FUNC_START;
    PRINT_VAR(_callback);
    delCallback(); 
    CLASS_FUNC_END;
}

void Caller::delCallback() 
{ 
    CLASS_FUNC_START;

    PRINT_VAR(_callback);
    if(_callback)
        delete _callback; 
    _callback = 0; 

    CLASS_FUNC_END;
}

void Caller::setCallback(Callback *cb) 
{ 
    CLASS_FUNC_START;

    if(_callback)
        delCallback(); 

    _callback = cb;
    PRINT_VAR(_callback);

    CLASS_FUNC_END; 
}

void Caller::call() 
{ 
    CLASS_FUNC_START;

    if (_callback) 
        _callback->run(); 
        
    CLASS_FUNC_END; 
}
//===========================================================================
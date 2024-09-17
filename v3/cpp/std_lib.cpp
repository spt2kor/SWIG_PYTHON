

//===========================================================================
#include "std_lib.h"
#include "Log.h"
//===========================================================================
#undef CLASS_NAME
#define CLASS_NAME "[STD_LIB]"
//===========================================================================
void Transform(double x[3]) {
    FUNC_START;
    
    for (int i = 0; i < 3; i++) {
        //printf("[%d] = %g\n", i, x[i]);
        PRINT_VAR(x[i]);
        x[i] += 10000;
    }
    FUNC_END;
}
// int Math::Add::add(int x,int y)
// {
//     FUNC_START;
//     m_x = x;
//     m_y = y;
//     m_sum = m_x + m_y;
//     FUNC_END;
//     return m_sum;
// }
// //===========================================================================
// //===========================================================================
// #undef CLASS_NAME
// #define CLASS_NAME "Callback"
// //===========================================================================
// Callback::~Callback()
// { 
//     CLASS_FUNC_START;
//     CLASS_FUNC_END;
// }
// void Callback::run() 
// {
//     CLASS_FUNC_START;
//     CLASS_FUNC_END;
// }
// Callback::Callback()
// {
//     CLASS_FUNC_START;
//     CLASS_FUNC_END;
// }
// void Callback::baseName()
// {
//     CLASS_FUNC_START;
//     CLASS_FUNC_END;
// }
// //===========================================================================
// //===========================================================================
// #undef CLASS_NAME
// #define CLASS_NAME "Caller"
// //===========================================================================
// //===========================================================================

// Caller::Caller(): _callback(0) 
// {
//     CLASS_FUNC_START;
//     CLASS_FUNC_END;
// }

// Caller::~Caller() 
// { 
//     CLASS_FUNC_START;
//     PRINT_VAR(_callback);
//     delCallback(); 
//     CLASS_FUNC_END;
// }

// void Caller::delCallback() 
// { 
//     CLASS_FUNC_START;

//     PRINT_VAR(_callback);
//     if(_callback)
//         delete _callback; 
//     _callback = 0; 

//     CLASS_FUNC_END;
// }

// void Caller::setCallback(Callback *cb) 
// { 
//     CLASS_FUNC_START;

//     if(_callback)
//         delCallback(); 

//     _callback = cb;
//     PRINT_VAR(_callback);

//     CLASS_FUNC_END; 
// }

// void Caller::call() 
// { 
//     CLASS_FUNC_START;

//     if (_callback) 
//         _callback->run(); 
        
//     CLASS_FUNC_END; 
// }
// //===========================================================================
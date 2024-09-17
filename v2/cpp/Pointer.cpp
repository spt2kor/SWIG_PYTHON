#include "Pointer.h"
#include "Log.h"
//===================================================================
FUNC ADD = addition;
FUNC SUBTRCT = subtraction;
FUNC MULTIPLY = multiplication;

//===================================================================
#undef CLASS_NAME
#define CLASS_NAME "[Pointer.h]"

//===================================================================


int execute_op(int a, int b, FUNC op ) {
  FUNC_START;
  auto res =  (*op)(a,b);
  FUNC_END;
  return res;
}
//===================================================================
int addition(int a, int b) {
  FUNC_START;
  PRINT_VAR(a);
  PRINT_VAR(b);
  auto res = a+b;
  PRINT_VAR(res);
  FUNC_END;
  return res;
}

int subtraction(int a, int b) {
  FUNC_START;
  PRINT_VAR(a);
  PRINT_VAR(b);
  auto res = a-b;
  PRINT_VAR(res);
  FUNC_END;
  return res;
}

int multiplication(int a, int b) {
  FUNC_START;
  PRINT_VAR(a);
  PRINT_VAR(b);
  auto res = a*b;
  PRINT_VAR(res);
  FUNC_END;
  return res;
}
//===================================================================

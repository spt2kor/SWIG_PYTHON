
//file:///C:/src/swigwin-4.1.1/Examples/perl5/funcptr/index.html
typedef int (*FUNC)(int,int);

int execute_op(int,int, FUNC op);
int addition(int,int);
int subtraction(int,int);
int multiplication(int,int);
extern FUNC ADD;
extern FUNC SUBTRCT;
extern FUNC MULTIPLY;
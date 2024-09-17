#pragma once
//------------------------------------------------------------
//------------------------------------------------------------
class Shape{

private:
    char* name;

    void privateFunc();

protected:
    
    void protctedFunc();

public:
    Shape(char* name = nullptr);
    virtual ~Shape();
    Shape(const Shape& src);
    
    Shape& operator= (const Shape &other);//NOTE:  does not work from perl 
    //Shape clone();//return a new object ,but it create multiple copies internally
    virtual void copy(const Shape &src);//copy from src to this object. both objects are already created

    virtual void show();
    void setName(const char* name);
    char* getName();
    static bool classInfo();// for singleton class
};
//NOTE : 
//base class virtual function does not work, no effect in perl client
//perl code can call derive non-virtual function too.
//polymorphism does not work, from perls prospective
//
//------------------------------------------------------------










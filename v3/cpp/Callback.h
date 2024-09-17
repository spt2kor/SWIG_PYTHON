# pragma once

namespace Math{
	int add(int x, int y);
	struct Add{
		int m_x = 1;
		int m_y = 2;
		int m_sum = 0;
		int add(int x,int y);
	};
}

//===================================================
class Callback {
public:
	Callback();
	virtual ~Callback() ;
	virtual void run() ;
	void baseName() ;
};
//===================================================

class Caller {
private:
	Callback *_callback;
public:
	Caller();	
	~Caller() ;
	void delCallback() ;
	void setCallback(Callback *cb);
	void call() ;
};
//===================================================
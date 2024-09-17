
# pragma once

//===================================================
//extern void Transform(int x[3]) ;

//===================================================
class StdLib {
public:
	StdLib();
	virtual ~StdLib() ;
	virtual void run() ;
	void baseName() ;
};
//===================================================

class DStdLib : public StdLib {
private:
	//vector<StdLib*> stdLibArr;
public:
	DStdLib();	
	~DStdLib() ;
	void delCallback() ;
	void setCallback(StdLib *cb);
	void call() ;
};
//===================================================

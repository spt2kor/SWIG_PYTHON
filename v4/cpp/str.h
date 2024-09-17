
# pragma once
#include <iostream>
#include <string>
using namespace std;

//===================================================
extern string moduleName;
//extern const string fileName;
static const string fileName = "str.h";
//===================================================

string UpdateStr(const string& perltxt );

void PrintStr(string perltxt );

string changePerlStr(string& perltxt ); //NOT Working

string* changePerlStrPtr(string* perltxt );
//===================================================

class StrTest {
public:
	string m_perltxt;
	static const string m_fileName;

	StrTest();
	virtual ~StrTest() ;
	string UpdateStr(const string& perltxt );
};
//===================================================

//===================================================

#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./generated_files/");
sys.path.append("./perl/");

import copy

import STDLib;

nl = '\n [PYTHON CODE] : ';

print ( nl," Testing Basic Python class testing String.i");

print ( nl, "******************************************** Print module  STDLib \n" );
print ( nl," STDLib =  ", STDLib);
print ( nl," type(STDLib)  =  ", type(STDLib) );
print ( nl," dir(STDLib)  =  ", dir(STDLib) );

print ( nl, "******************************************** global extern string moduleName;" );

print ( nl," STDLib.cvar.moduleName =  ", STDLib.cvar.moduleName);
print ( nl, "******************************************** static const string fileName = \"str.h\"; " );
print ( nl," STDLib.cvar.fileName =  ", STDLib.cvar.fileName);

print ( nl, "******************************************** : string UpdateStr(const string& perltxt );" );

s1 = "%this is a Python String%";
s2 = STDLib.UpdateStr(s1);
print ( nl," s2 = STDLib.UpdateStr(s1);  ", s2);

print ( nl, "******************************************** : void PrintStr(string perltxt ); " );

s2 = STDLib.PrintStr(s1);
print ( nl," s2 = STDLib.PrintStr(s1);  ", s2);
print ( nl, "******************************************** : string changePerlStr(string& perltxt );  " );

s2 = STDLib.changePerlStr(s1);
print ( nl," s2 = STDLib.changePerlStr(s1);  ", s2);

print ( nl," s1 ;  ", s1);
#NOTE: it ignores the C++ changes to python string&, 
#it means python string is making copy in C++ as string&

print ( nl, "******************************************** : string* changePerlStrPtr(string* perltxt ); " );

s2 = STDLib.changePerlStrPtr(s1);
#NOTE: make: *** [str] Segmentation fault, if we do perltxt[3] = '#';  in C++
#if we try to modify the string* in C++, it gives segmentation fault.
# so python string* is constant.

print ( nl," s2 = STDLib.changePerlStrPtr(s1);  ", s2);
print ( nl," s1 ;  ", s1);
print ( nl, "******************************************** using class STDLib.StrTest() " );

r1 = STDLib.StrTest();
print ( nl," r1.m_perltxt =  ", r1.m_perltxt);

r1.m_perltxt = "modified python string";
print ( nl," r1.m_perltxt =  ", r1.m_perltxt);

print ( nl," r1.m_fileName =  ", r1.m_fileName);

s3 = r1.UpdateStr("Test String from Python");
print ( nl,"s3 = r1.UpdateStr(\"Test String from Python\");  ", s3);

print("----------------------")


del r1;

print (nl, "***********  END OF PROGRAM *********************************");

# pragma once
#include <iostream>
#include <string>
#include <vector>

using namespace std;
//===================================================
//https://www.swig.org/Doc4.0/SWIGDocumentation.html#Library_std_vector


double average(std::vector<int> v);

std::vector<double> half(const std::vector<double>& v) ;

void halve_in_place(std::vector<double>& v) ;


//===================================================
bool operator==(const std::vector<double>& v1 , const std::vector<double>& v2 );
//===================================================
//===================================================

//===================================================

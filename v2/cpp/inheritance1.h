
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

//https://www.swig.org/Doc4.0/SWIGPlus.html#SWIGPlus_target_language_callbacks

class Employee {
private:
	std::string name;
public:
	Employee(const char* n): name(n) {std::cout<< " \t["<< this <<"]\t"<<name <<std::endl;
	}
	virtual std::string getTitle() { return getPosition() + " " + getName(); }
	virtual std::string getName() { return name; }
	virtual std::string getPosition() const { return "Employee"; }
	virtual ~Employee() { //std::cout<< " \t["<< this <<"]\t"<<this->getTitle() <<"\t:" <<std::endl; 
	printf("~Employee() @ %p\n", (void *)this); }
};


class Manager: public Employee {
public:
	Manager(const char* n): Employee(n) {}
	virtual std::string getPosition() const { return "Manager"; }
};


class EmployeeList {
	std::vector<Employee*> list;
public:
	EmployeeList() {
		list.push_back(new Employee("Bob"));
		list.push_back(new Employee("Jane"));
		list.push_back(new Manager("Ted"));
	}
	void addEmployee(Employee *p) {
		list.push_back(p);
		std::cout << "New employee added.   Current employees are:" << std::endl;
		std::vector<Employee*>::iterator i;
		for (i=list.begin(); i!=list.end(); i++) {
			std::cout << "  " << (*i)->getTitle() << std::endl;
		}
	}
	const Employee *get_item(int i) {
		return list[i];
	}
	~EmployeeList() { 
		std::vector<Employee*>::iterator i;
		std::cout << "~EmployeeList, deleting " << list.size() << " employees." << std::endl;
		for (i=list.begin(); i!=list.end(); i++) {
			delete *i;
		}
		std::cout << "~EmployeeList empty." << std::endl;
	}
};


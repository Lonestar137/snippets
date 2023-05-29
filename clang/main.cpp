#include <iostream>
//using std::string; // if you want to set namespace for a specific obj
using namespace std;

/*
 * Dependency Notes:
 * Dependencies will have .lib or .dll files.   .lib is static meaning when it's linked, it's compiled with your code.
 * + encapsulation
 * - slower compile time
 * 
 * DLL is dynamic lib, meaning your program will need to be installed on a system with access to these files.
 * + faster compile time
 * - less encapsulation

*/

class Test{
    // by default, fields are private
    string FieldOne;
    int    FieldTwo;
    
    public:
        // initializer
        void init(string fieldOne, int fieldTwo){
            FieldOne = fieldOne;
            FieldTwo = fieldTwo;
            printf("\nSet fields.\n");
        }
        
        // retrieve a private field
        string getFieldOne(){
            std::cout << FieldOne << std::endl;
            return FieldOne;
        }
};

class Employee{
    public:
        string Name;
        string Company;
        int Age;
        
        void IntroduceYourself(){
            std::cout << "Name: " << Name << std::endl;
            std::cout << "Company: " << Company << std::endl;
            std::cout << "Age: " << Age << std::endl;
        }
};

class WithConstructor{
    private: // this line is optional.  Private by default, it's just for readability.
        string Name;
        int     Age;
    protected: // protected objects are only available inside classes that inherit from this one.
        string OnlyAvailInChildren;
    public:
        /*
         * Constructor rules
         * 1. Same name as class
         * 2. No return type(not even void)
        */ 
        WithConstructor(string name, int age){
            Name = name;
            Age = age;
        }
        
        void ListPrivateVariables(){
            cout << Name << endl;
            cout << Age << endl;
        }
    
};

class InheritanceExample : WithConstructor{
    string Name, LastName;
    int Age;
    public:
        // NOTE: on the constructor we have to pass the values that we didn't inherit to the parent constructor here.
        InheritanceExample(string inheritedVar, string lastName) : WithConstructor(Name, Age){
            Name = "generic Name"; // these values get passed to WithConstructor's constructor
            Age = 30; // <------------^
            LastName = lastName;
            OnlyAvailInChildren = inheritedVar;
        }

        void printVariables(){
            cout << "Inherited variable: " << OnlyAvailInChildren << endl;
            cout << "Last Name: " << LastName << endl;
        }
};

void classExamples(){
    Employee Me;
    Me.Name = "John Doe";
    Me.Age = 21;
    Me.Company = "SomeCompany";
    
    Me.IntroduceYourself();
    

    Test t;
    t.init("Setting a private field", 365);
    t.getFieldOne();

    
    WithConstructor obj = WithConstructor("World", 100);
    obj.ListPrivateVariables();
    
    InheritanceExample obj2 = InheritanceExample("inherited", "lname");
    // obj2.ListPrivateVariables(); <-- BEWARE: of this in inheritance.  The child class is missing some variables for this public function.
    obj2.printVariables();
}

int main(){
    classExamples();

    printf("Testing\n");
    return 0;
}
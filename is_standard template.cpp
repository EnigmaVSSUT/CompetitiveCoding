// C++ program to illustrate 
// std::is_standard_layout  template 
  
#include <iostream> 
#include <type_traits> 
using namespace std; 
  
// Class with local variable 
class gfg { 
    int variab; 
}; 
  
// Structure with local variable 
struct sam { 
    int variab; 
  
private: 
    int variab_priv; 
}; 
  
// Empty union 
union raj { 
}; 
  
// Driver code 
int main() 
{ 
    cout << boolalpha; 
    cout << "Is gfg class a standard layout: "
         << is_standard_layout<gfg>::value << '\n'; 
    cout << "Is structure sam a standard layout: "
         << is_standard_layout<sam>::value << '\n'; 
    cout << "Is union raj a standard layout: "
         << is_standard_layout<raj>::value << '\n'; 
    cout << "Is datatype char a standard layout: "
         << is_standard_layout<char>::value << '\n'; 
    cout << "Is integer array 'int a[10]' a standard layout: "
         << is_standard_layout<int[10]>::value << '\n'; 
  
    return 0; 
} 


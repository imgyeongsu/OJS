#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double cmPft = 30.48;
    int cmPmi = 160934;

    double ft, mile;
    ft = 9.2;
    mile = 1.3;

    cout << fixed;
    cout.precision(1);
    cout << ft << "ft" << " = " << ft * cmPft <<"cm\n";
    cout << mile << "mi" << " = " << mile * cmPmi << "cm";
    
    return 0;
}
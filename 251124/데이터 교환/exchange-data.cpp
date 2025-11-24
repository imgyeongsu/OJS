#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 5;
    int b = 6;
    int c = 7;
    int temp = b; // temp : 6
    b = a; // b = 5
    int temp2 = c;
    c = temp; // c = 6
    a = temp2; 

    cout  << a << '\n' << b <<'\n'<< c;



    return 0;
}
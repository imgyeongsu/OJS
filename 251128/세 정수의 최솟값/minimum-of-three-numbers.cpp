#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c, min;
    cin >> a >> b >> c;
    if (a < b){
        min  = a;
    } else {
        min = b;
    }
    if ( min > c){
        min = c;
    }
    
    cout << min;
    return 0;
}
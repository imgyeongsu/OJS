#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    if (a <= b && b <= c){
        cout << b;
    } else if ( b <= a && a <= c) {
        cout << a;
    } else {
        cout << c;
    }
    return 0;
}
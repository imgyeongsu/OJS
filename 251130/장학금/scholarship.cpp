#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int m, f;
    cin >> m >> f;
    if (m >= 90){
        if (f >= 95){
            cout << 100000;
        } else if ( f>= 90) {
            cout << 50000;
        } else {
            cout << 0;
        }
    } else {
        cout << 0;
    }
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c, maxv;
    cin >> a >> b >> c;
    if (a > b){
        maxv = a;
    } else {
        maxv = b;
    }

    if (maxv < c){
        maxv = c;
    }
    
    cout << maxv;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);
    if (a > b) swap(a, b); 
    cout << b;

    return 0;
}
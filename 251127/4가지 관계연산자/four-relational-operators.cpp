#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    char c = '\n';

    cout << (a >= b) << c;
    cout << (a > b) << c;
    cout << (b >= a) << c;
    cout << (b > a);

    return 0;
}
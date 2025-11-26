#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double a, b;
    cin >> a >> b;
    double c = (a + b) / (a - b);
    cout << fixed;;
    cout.precision(2);
    cout << c;
    return 0;
}
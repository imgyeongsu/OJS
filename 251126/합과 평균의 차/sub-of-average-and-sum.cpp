#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    int hap = a + b + c;
    int avg = hap /3;
    cout << hap << '\n' << avg << '\n' << hap-avg;
    return 0;
}
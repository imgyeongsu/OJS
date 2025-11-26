#include <iostream>
using namespace std;

int bmi(int h, int w){
    return 10000 * w / h / h;
}

int main() {
    // Please write your code here.
    int h, w;
    cin >> h >> w;
    int b = bmi(h, w);
    cout << b;
    if (b>=25){
        cout << "\nObesity";
    }

    return 0;
}
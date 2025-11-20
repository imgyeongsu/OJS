#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    while (true) {
        if (a > b){
            break;
        }
        cout << a << ' ';
        if (a % 2) { // 홀수라면
            a *= 2;
        } else {
            a += 3;
        }
    }
    return 0;
}
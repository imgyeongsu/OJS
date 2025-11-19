#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B ,C;
    cin >> A >> B >> C;
    if (A > B) {
        swap(A, B);
    }
    if (A > C) {
        swap(A, C);
    }
    if (B > C) {
        swap(B, C);
    }
    cout << B;

    return 0;
}
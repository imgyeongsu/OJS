#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int m1, e1, m2, e2;
    cin >> m1 >> e1 >> m2 >> e2;
    if (m1 > m2){
        cout << 'A';
    } else if (m2 > m1) {
        cout << 'B';
    } else {
        if (e1 > e2) {
            cout << 'A';
        } else {
            cout << 'B';
        }
    }
    return 0;
}
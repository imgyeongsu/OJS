#include <iostream>
using namespace std;

int abs(int n){
    if (n < 0){
        return -n;
    }
    return n;
}

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    cout << abs(a-b);
    return 0;
}
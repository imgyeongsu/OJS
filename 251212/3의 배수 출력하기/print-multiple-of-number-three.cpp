#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    n /= 3;
    int i = 0;
    while (++i <= n){
        cout << 3 * i << ' ';
    }
    return 0;
}
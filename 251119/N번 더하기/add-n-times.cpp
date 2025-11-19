#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, n;
    cin >> a >> n;
    for (int i=1; i<n+1; i++) {
        cout << a + n * i << '\n';
    }

    return 0;
}
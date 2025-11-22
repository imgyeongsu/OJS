#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n = 4;
    int x;
    for (int r=0; r < n; r++){
        int hap = 0;
        for (int c =0; c < n; c++){
            cin >> x;
            hap += x;
        }
        cout << hap << '\n';
    }

    return 0;
}
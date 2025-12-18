#include <iostream>

using namespace std;

int n, m;

int main() {
    cin >> n >> m;

    // Please write your code here.
    for(int i =0; i<n; i++){
        for (int ii = 0; ii< m; ii++){
            cout << '1';
        }
        cout << '\n';
    }

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n = 3;
    int arr[2][n][n];

    int v;

    for (int i =0; i<2; i++){
        for (int r=0; r<n; r++){
            for (int c=0; c<n; c++){
                cin >> v;
                arr[i][r][c] = v;
            }
        }
    }
    for (int r=0; r < n; r++){
        for(int c=0; c < n; c++){
            cout << arr[0][r][c] * arr[1][r][c] << ' ';
        }
        cout << '\n';
    }

    return 0;
}
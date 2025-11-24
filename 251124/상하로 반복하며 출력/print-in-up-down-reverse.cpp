#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[n][n];
    int cnt = 0;

    for (int c=0; c <n; c++){
        for (int r=0; r<n; r++){
            if (c % 2 == 0){
                arr[r][c] = cnt % n + 1;
                cnt ++;
            } else {
                arr[n-r-1][c] = cnt % n + 1;
                cnt ++;
            }
        }
    }

    for (int r=0; r<n; r++){
        for (int c=0; c<n; c++){
            cout << arr[r][c];
        }
        cout << '\n';
    }



    return 0;
}
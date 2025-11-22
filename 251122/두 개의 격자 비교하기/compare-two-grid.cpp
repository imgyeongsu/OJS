#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int N, M;
    cin >> N >> M;
    int arr[2][N][M];

    int v;
    for (int i=0; i<2; i++){

        for (int r=0; r<N; r++){
            for (int c=0; c<M; c++){
                cin >> v;
                arr[i][r][c] = v;
            }
        }
    }


    for (int r=0; r<N; r++){
        for (int c=0; c<M; c++){
            if (arr[0][r][c] == arr[1][r][c]){
                cout << 0 << ' ';
            } else {
                cout << 1 << ' ';
            }
        }
        cout << '\n';
    }

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;

    for (int i=0; i<N; i++){
        for (int ii =1; ii<N+1; ii++){
            if (i % 2 == 0){ // 짝수 행일때
                cout << ii;
            } else {
                cout << N + 1 - ii;
            }
        }
        cout << '\n';
    }

    return 0;
}
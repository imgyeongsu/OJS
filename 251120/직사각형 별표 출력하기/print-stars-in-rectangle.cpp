#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, M;
    cin >> N >> M;
    for (int i = 0; i < N; i ++){
        for (int ii = 0; ii < M; ii ++){
            cout << "* ";
        }
        cout << '\n';
    }
    return 0;
}
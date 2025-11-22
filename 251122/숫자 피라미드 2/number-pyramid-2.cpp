#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 1;
    int N;
    cin >> N;
    for (int i = 1; i < N+1; i++){
        for (int j=0; j <i; j++){
            cout << cnt << ' ';
            cnt ++;
        }
        cout << '\n';
    }
    return 0;
}
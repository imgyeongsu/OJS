#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int x;
    int cnt = 0;
    for (int i = 0; i < 16; i++){
        cin >> x;
        if (x % 5 == 0){
            cnt ++;
        }
    }
    cout << cnt;
    return 0;
}
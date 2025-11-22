#include <iostream>

using namespace std;

int st, ed;

int main() {
    cin >> st >> ed;
    // Please write your code here.
    int cnt = 0;
    for (int i = st; i < ed + 1; i++){
        bool is_three = false;
        for (int ii = 2; ii < i; ii++){
            if (i % ii == 0){
                if (i / ii == ii){
                    is_three = true;
                    // cout << i;
                } else {
                    break;
                }
            }
        }
        if (is_three) {
            cnt ++;
        }
    }
    cout << cnt;

    return 0;
}

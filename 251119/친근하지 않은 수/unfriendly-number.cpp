#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int ans = 0;
    for (int i = n; i > 0; i--){
        if (i%2==0){
            continue;
        } else if (i % 3 == 0){
            continue;
        } else if (i % 5 == 0){
            continue;
        }
        ans ++;
    }
    cout << ans;

    return 0;
}
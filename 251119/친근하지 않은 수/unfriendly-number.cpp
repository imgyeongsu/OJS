#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int ans = 0;
    while (n-->0){
        if (n%2==0){
            continue;
        } else if (n % 3 == 0){
            continue;
        } else if (n % 5 == 0){
            continue;
        }
        ans ++;
    }
    cout << ans;

    return 0;
}
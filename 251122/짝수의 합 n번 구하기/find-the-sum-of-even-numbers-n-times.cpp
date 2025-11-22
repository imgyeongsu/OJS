#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (int i = 0; i < N; i++){
        int a, b, ans;
        cin >> a >> b;
        ans = 0;
        for (int ii = a; ii < b+1; ii++){
            if (ii % 2 == 0){
                ans += ii;
            }
        }
        cout << ans << '\n';
    }

    return 0;
}
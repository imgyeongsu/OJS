#include <iostream>
using namespace std;

int main() {
   // Please write your code here.
    int ans =0;
    int x;
    for (int r=0; r<4; r++){
        for(int c=0; c < 4; c++){
            cin >> x;
            if (c < r+1){
                ans += x;
            }
        }
    }
    cout << ans;
    return 0;
}